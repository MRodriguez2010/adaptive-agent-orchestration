# Orchestration policy

This policy combines a stable Main coordinator with temporary Supervisor ownership of difficult work. The purpose is to complete useful work with clear control, appropriate patience, and inspectable outcomes.

## Assignment contracts and temporary responsibility

A contract is an operational assignment: objective, inputs, allowed scope, authority, acceptance evidence, resource boundaries, and a condition for ending responsibility. Bring in a specialist when the task is difficult or blocked and the specialist materially helps; a failed attempt is not required. A specialist who returns advice or a bounded artifact is a worker. Transferring control of the affected plan and workers is Supervisor takeover.

After delivery is accepted, reconcile or explicitly transfer live operations, close the assignment, and release its authority. A retained idle agent needs a new assignment before doing further work. Ending the assignment does not mean deleting its evidence or assuming that its external operations stopped.

Related defects need triage against the assigned acceptance criteria. A direct dependency may justify correction within the existing contract and permissions only if it prevents verification or safe handback of the assigned blocker. A dependency of Main's later work belongs in the report for Main. Preventive review does not authorize unrelated cleanup or prove that a future delay was prevented.

See [execution modes](EXECUTION-MODES.md) for changing task structure under one state and authority layer, and [related work](RELATED-WORK.md) for established precedents and contribution boundaries.

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

A known difficult scope may justify stronger supervisory planning before failed attempts when evidence establishes a capability or architectural need. Difficulty alone does not require a second coordinator; use a bounded specialist worker when advice or a narrow deliverable is sufficient.

The deployment should define task-specific trigger examples and review their effectiveness. Illustrative counts are starting points, not universal failure thresholds. Never wait for every time budget to expire merely to qualify for supervision.

A known permission barrier, required user decision, hard resource ceiling, or confirmed external outage follows its appropriate access, recovery, or stopping path. Escalate when diagnosis or coordination can help; a more expensive model is not the default response to every blocked state. An undersized soft timer should prompt evidence-based budget review before the operation is classified as failed.

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

Give the supervisory phase a finite recovery budget, an observable milestone, and a stopping condition within the task's remaining resources. If recovery makes no useful progress and there is no justified alternative, checkpoint as unresolved and identify the actual blocker or required decision. Changing the model, worker, or coordinator never resets attempts, elapsed resource use, or the incident's history.

### Stop at the assigned resolution

Record the blocker's in-scope and out-of-scope work, acceptance checks, permitted direct dependencies, and return condition before takeover. Use the [Supervisor assignment](../templates/supervisor-assignment.md) and [handoff](../templates/handoff.md) templates. The Supervisor cannot award itself follow-up work or broaden the completion criteria as it discovers issues.

Classify a new finding using its evidence. Work on it inside the existing assignment only if it directly prevents a declared blocker check or reconciliation needed for safe handback, and the correction is already authorized. A general improvement, unrelated defect, or dependency of the next Main task does not meet that condition. Return those findings with evidence, likely impact, why they are outside the assignment, and a proposed check or follow-up. Leave their disposition to Main.

Once the declared blocker checks pass and owned operations are reconciled or explicitly transferred, stop investigation and initiate handback. Deferred findings do not make that resolution incomplete. Main may handle them itself, defer them, or create another bounded contract when the overall task warrants it. That decision does not require another user approval when existing authority covers it, and it does not keep the completed Supervisor assignment active.

Use a finite handback/acknowledgment limit within remaining resources. While waiting for Main's acceptance, the Supervisor is quiescent except for handback communication and necessary safety work on already-owned operations. An unavailable recipient leads to a checkpoint and the declared safe fallback, not another investigation or repeated self-extension. Transfer authority only after the acceptance and ownership checks pass.

## 5. Progress-aware limits

| Budget | What it measures | Typical evidence |
|---|---|---|
| Startup | Time to acquire and initialize required resources | Loading stages, queue position, initialization logs |
| Execution | Time spent doing the assigned operation | Completed work units, output changes, test phases |
| Inactivity | Absence of a meaningful observable milestone | Last useful output or state transition |
| Overall resources | Total time, tokens, money, calls, concurrency or reserved capacity | External accounting and owner policy |
| Observation | How long one status/read request may wait | The observation result, not the job's final outcome |
| Retry | Attempts for a logical operation and failure mode | Confirmed transient failures, changed inputs and retained attempt records |
| Supervisory recovery | Resources reserved for the temporary recovery phase within the task ceiling | A stated next milestone, remaining resources and a recovery stop condition |

Choose limits from the workload and observed behavior. A long build, model startup, repository operation, and short status request should not share one arbitrary timer.

Before execution, record concrete finite starting limits, the objective and acceptance criteria, and the next milestone in the durable task record. Use human-readable project files when the host provides file access. Reuse configured values; when values are absent, select generous finite task-appropriate limits within existing authority. There is no universal short timeout or fixed retry count. An unset configuration example means limits still need selection, not permission for an unbounded run. Identify which limits the host enforces and which remain advisory.

A soft timeout or retry threshold is a review point. Inspect executor evidence to distinguish healthy slow work, genuine failure, inactivity and uncertain delivery. An undersized soft threshold may be revised with evidence and authority within the remaining finite task ceiling. User-set hard limits remain binding until an authorized decision changes them. Budget exhaustion does not establish that a test failed or that an already-dispatched operation stopped.

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

Exhausting an operation's retry budget ends the unchanged strategy. A materially different approach or a new attempt after changed inputs or a meaningful correction may be justified within the remaining authorized budget, with all prior attempts retained. A handoff, model change or rephrased command cannot reset counters or the task ceiling. This preserves both bounded recovery and the ability to repeat a valid check after its inputs change.

## 7. Verification and handback

The blocker is resolved when its defined acceptance condition passes. Match verification to the consequence of the change: inspect saved artifacts, run relevant checks, observe the actual target environment, and use an independent check where it materially improves confidence.

Handback includes the cause, exact change, evidence, limitations, deferred findings, worker/operation state, remaining resources and next step. Main checks the assigned blocker's evidence and explicitly accepts control. The runtime advances the ownership generation, invalidates stale assignment authority, closes the temporary supervisory phase and makes the Supervisor inactive. A retained session or process carries no authority and must issue no further searches, checks, assignments, polling or mutations until a new scoped assignment requires it.

A passing narrow blocker check does not automatically complete the user's entire task. Main automatically resumes remaining already-authorized implementation, integration, delivery or user-facing verification without another user "continue" request. The host must actually support recipient activation and continuation delivery; otherwise record that limitation and the next step rather than claiming Main resumed. Preserve operation identities and reconcile uncertain continuation delivery before retrying it.

If acceptance fails, Main identifies the exact failed blocker criterion, missing required evidence or unreconciled owned operation. Supervisor retains the incident, records the new evidence and changes strategy within its authorized scope and remaining budget. Unrelated findings cannot expand those criteria or keep supervision active. It must not reset the task's overall resource accounting. Ask the user when a real decision, access requirement, or material resource/scope change cannot be resolved autonomously.

## 8. Status and evidence

Use explicit states: planned, dispatched, running, execution-unknown, blocked, failed, cancelled, verified and complete. Keep operation outcomes separate from overall task outcomes. A cancelled task may contain a retained earlier failure; a completed dispatch may have an unverified execution outcome.

Every significant state transition should reference evidence and identify the acting role. Retain actual model/effort/run metadata when available, original failures, accepted source/artifact identities, and any remaining uncertainty. Avoid storing secrets in shared packets or public reports.

## 9. Evaluate the orchestration

Track verified end-to-end completion, recurrence of the same blocker, time blocked, total resource use per resolved issue, duplicate side effects, unnecessary escalation, and false-stall decisions. Compare like-for-like tasks before claiming that a model or policy is better. More agent activity or more supervisor interventions are not success metrics.

See [evaluation scenarios](EVALUATION.md), the [runtime contract](RUNTIME-CONTRACT.md), and reusable [handoff](../templates/handoff.md), [handback](../templates/handback.md), and [worker assignment](../templates/worker-assignment.md) templates.
