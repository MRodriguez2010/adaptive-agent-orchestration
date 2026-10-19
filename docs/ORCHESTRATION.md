# Orchestration policy

This policy combines a stable Main coordinator with temporary Supervisor ownership of difficult work. The purpose is to complete useful work with clear control, appropriate patience, and inspectable outcomes.

## 1. Roles and scope

| Role | Responsibility | Control boundary |
|---|---|---|
| Main | Understand the request, maintain continuity, coordinate routine work, communicate with the user, accept handback and deliver the result | Owns normal orchestration and the overall user commitment |
| Supervisor | Diagnose and resolve a specific blocker; plan and coordinate affected workers; synthesize and validate the resolution | Temporarily owns the affected scope after an explicit transfer |
| Worker | Perform a narrowly assigned task and return results with evidence | Owns only its assignment and declared files/resources |
| Runtime | Store authoritative state, enforce ownership and permissions, execute operations, retain evidence, and account for resources | Enforces boundaries independently of model prose |

Main and Supervisor are roles. A deployment may map them to different models, different reasoning settings, or separate agents. Select models using demonstrated task performance and cost. Stronger reasoning may help diagnosis; it does not provide missing access, repair an unavailable service, or establish that a command executed.

During escalation, Main may continue unrelated work. It must not issue competing instructions to the same workers or mutate the same affected resources. A Supervisor's authority is limited to the granted scope; escalation grants no additional permissions.

## 2. Escalation triggers

Escalate when evidence indicates a problem that the current approach is unlikely to resolve efficiently:

- The same underlying failure returns after a meaningful correction.
- Different components or agents report incompatible states.
- Execution may have occurred, but delivery or ownership is uncertain and ordinary reconciliation cannot establish the outcome.
- The blocker spans architecture, integration, shared state, or several dependent components.
- Attempts produce activity without reducing uncertainty or satisfying a milestone.

Do not make the number of failed tool calls the sole trigger. A malformed command, ordinary assertion failure, or unsuccessful search often needs a local correction. A serious ownership ambiguity can justify immediate escalation.

The deployment should define task-specific trigger examples and review their effectiveness. Illustrative counts are starting points, not universal failure thresholds. Never wait for every time budget to expire merely to qualify for supervision.

## 3. Transfer ownership safely

Use these steps for each transfer:

1. Main records the escalation reason and prepares the handoff packet.
2. Reconcile or safely pause affected in-flight work. Healthy operations may keep running with explicit identities and a declared result destination.
3. The runtime transfers the scope's control record atomically and advances its generation/fencing token.
4. Supervisor acknowledges the current record and accepts ownership.
5. Affected workers accept assignments only from that scope's current orchestrator and generation.

A lease expiring does not prove that its former holder or an external operation stopped. Fence new conflicting mutations and establish actual operation state before takeover. Receiving a late result is allowed as evidence; granting it current orchestration authority is a separate decision.

An application that lacks these mechanisms should describe ownership as a cooperative convention and serialize affected actions. It must not advertise an enforced mutex or exactly-once execution.

## 4. Supervisor operation

Start with evidence. Separate established facts from hypotheses and identify the next observation that can distinguish competing causes. Reuse existing workers or add a narrowly scoped specialist when it helps. Avoid repeating the full investigation when the retained evidence already answers a question.

Each assignment declares the objective, inputs, allowed mutations, acceptance criteria, expected evidence, operation identity, and conditions for stopping or escalating. Parallel work must have independent outputs or explicit isolation. Dependent work starts after its required input is available.

Use the highest reasoning setting when the blocker warrants it and the configured budget permits it. There is no required ladder through every intermediate setting. Use appropriate lower-cost workers for clear implementation, documentation, or targeted verification.

Keep a single incident record. A recurrence adds evidence and attempts to that record. Repeated takeover/handback without a stable resolution is itself a reason to reassess the strategy, not to create another supervisor hierarchy.

## 5. Progress-aware limits

| Budget | What it measures | Typical evidence |
|---|---|---|
| Startup | Time to acquire and initialize required resources | Loading stages, queue position, initialization logs |
| Execution | Time spent doing the assigned operation | Completed work units, output changes, test phases |
| Inactivity | Absence of a meaningful observable milestone | Last useful output or state transition |
| Overall resources | Total time, tokens, money, calls, concurrency or reserved capacity | External accounting and owner policy |
| Observation | How long one status/read request may wait | The observation result, not the job's final outcome |

Choose limits from the workload and observed behavior. A long build, model startup, repository operation, and short status request should not share one arbitrary timer.

A soft-budget extension records the evidence, reason, authorized upper bound, next milestone, and action if the milestone does not arrive. An extension that changes live execution authority must be accepted by the runtime before the old authority expires. A model cannot extend a worker by merely announcing it.

Keep hard permission and resource boundaries outside the model. At a hard boundary, checkpoint and follow the declared cancellation/cleanup protocol. Preserve the observed outcome, including unknown execution, failed validation, or incomplete cleanup. Do not convert these states to success.

Heartbeats, process existence, and streaming tokens are liveness signals. Useful progress includes completed loading stages, a new verified finding, a corrected artifact, a relevant test advancing, or a completed dependency. Repeated commentary is not evidence of progress.

## 6. Failure classification and recovery

| Situation | Required response | Avoid |
|---|---|---|
| Healthy operation is slow | Observe at a suitable interval; adapt a soft budget with evidence | Cancelling merely because a short poll ended |
| Transport reply is lost | Mark delivery/outcome unknown; query durable state using the same operation identity | Issuing the mutation again immediately |
| Test or calculation fails | Retain output; correct the cause; run relevant checks | Increasing a timeout to hide a real failure |
| Read fails transiently | Use an appropriate bounded observation retry | Treating every read retry as a new execution attempt |
| Policy or permission denial | Diagnose the mismatch or obtain necessary authority | Repeatedly trying to bypass the denial |
| Same command after changed inputs | Permit it when the change and authority justify it; retain both outcomes | A lifetime duplicate ban based only on command text |
| No relevant state/input change and same failure | Stop the unchanged strategy; change approach or escalate | Rephrasing the same action and resetting counters |
| Worker/controller disappears | Reconcile worker and external-operation state; fence uncertain mutations | Assuming controller death proves all children stopped |

A retry is a new attempt. Record why it is justified and relate it to the prior operation. For side effects, use idempotency/deduplication where supported and state reconciliation where it is not. Do not claim exactly-once behavior unless the underlying service actually provides the required guarantees.

## 7. Verification and handback

The blocker is resolved when its defined acceptance condition passes. Match verification to the consequence of the change: inspect saved artifacts, run relevant checks, observe the actual target environment, and use an independent check where it materially improves confidence.

Handback includes the cause, exact change, evidence, limitations, worker/operation state, remaining resources and next step. Main checks the evidence and explicitly accepts control. The runtime advances the ownership generation, invalidates stale assignment authority, and closes the temporary supervisory phase.

A passing narrow blocker check does not automatically complete the user's entire task. Main resumes remaining implementation, integration, delivery or user-facing verification.

If acceptance fails, Supervisor retains the incident, records the new evidence and changes strategy within its authorized scope. It must not reset the task's overall resource accounting. Ask the user when a real decision, access requirement, or material resource/scope change cannot be resolved autonomously.

## 8. Status and evidence

Use explicit states: planned, dispatched, running, execution-unknown, blocked, failed, cancelled, verified and complete. Keep operation outcomes separate from overall task outcomes. A cancelled task may contain a retained earlier failure; a completed dispatch may have an unverified execution outcome.

Every significant state transition should reference evidence and identify the acting role. Retain actual model/effort/run metadata when available, original failures, accepted source/artifact identities, and any remaining uncertainty. Avoid storing secrets in shared packets or public reports.

## 9. Evaluate the orchestration

Track verified end-to-end completion, recurrence of the same blocker, time blocked, total resource use per resolved issue, duplicate side effects, unnecessary escalation, and false-stall decisions. Compare like-for-like tasks before claiming that a model or policy is better. More agent activity or more supervisor interventions are not success metrics.

See [evaluation scenarios](EVALUATION.md), the [runtime contract](RUNTIME-CONTRACT.md), and reusable [handoff](../templates/handoff.md), [handback](../templates/handback.md), and [worker assignment](../templates/worker-assignment.md) templates.
