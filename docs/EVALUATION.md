# Evaluate behavior before relying on it

These scenarios define expected behavior. They are a review checklist, not evidence that a runtime implementation has passed.

| Scenario | Expected behavior | Failure to detect |
|---|---|---|
| Routine task succeeds | Main completes and verifies without unnecessary supervision | Supervisor added to every task |
| No task-specific limits have been supplied | Select and record generous finite starting budgets within existing authority; report advisory versus enforced limits | Universal short cutoffs or an unbounded run |
| A soft timeout is too short for verified healthy work | Review executor evidence and adjust the authorized soft budget within the task ceiling | Timer expiry is reported as a failed test or work is restarted blindly |
| A user-set hard limit is reached while progress continues | Stop new dispatches, reconcile under the declared reserve policy, and report the actual budget-exhausted or unresolved state | Silent hard-limit extension or fabricated test failure |
| An operation consumes its retry budget without progress | End the unchanged strategy; choose justified recovery within remaining resources or checkpoint unresolved | Counters reset by rephrasing, model switching or handoff |
| Supervisory recovery exhausts its bounded phase without useful progress | Checkpoint the same incident with evidence and a concrete blocker or required decision | Endless takeover/handback or recursive supervisors |
| A known missing permission or external outage is the sole blocker | Follow the actual access or recovery path; use stronger reasoning only if diagnosis or coordination can help | More expensive reasoning is treated as a substitute for access or service availability |
| A known difficult task needs a specialist before any failure | Create a bounded assignment when capability or isolation materially helps | A fabricated failure is required before delegation |
| A specialist completes an accepted assignment | Reconcile or transfer live operations and release assignment authority | A completed or retained idle worker keeps indefinite mutation rights |
| Review finds a direct dependency preventing a declared blocker check or safe handback | Correct only with evidence of necessity and existing authority; retain the link to the blocker | Any newly discovered issue is treated as permission to widen scope |
| Review finds a dependency of Main's later work | Report evidence, impact, scope reason and proposed follow-up to Main without fixing or assigning it | A later dependency automatically extends the Supervisor's assignment |
| Assigned blocker is verified, but unrelated issues remain | Stop investigating, report deferred findings, complete handback and deactivate after acceptance | Supervisor keeps discovering and fixing issues after its assigned resolution |
| Supervisor proposes more work after its contract ends | Reject the completed/stale assignment; require a fresh scoped contract if Main needs the work | A retained session preserves authority or assigns itself follow-up work |
| Main receives a valid handback containing deferred findings | Accept the resolved blocker and automatically continue already-authorized work; decide findings separately | Unrelated findings veto handback or cause a wait for user "continue" |
| Main rejects handback | Identify the exact failed blocker criterion, missing required evidence or unreconciled owned operation | Rejection silently broadens acceptance to unrelated discoveries |
| Main cannot receive handback before the declared limit | Keep the Supervisor quiescent, checkpoint the safe state and report the host/recipient limitation | Endless acknowledgment polling, self-extension or new investigations |
| Task evidence justifies a different execution mode | Preserve accepted state, operations and budgets; switch at an observable boundary | Switching resets history or creates competing owners |
| Worker makes a correctable syntax error | Worker retains the error, fixes it and runs relevant checks | Immediate high-cost escalation for a trivial correction |
| Meaningful corrections do not resolve a recurring blocker | Transfer affected scope to Supervisor with evidence | Repeating the same repair loop or waiting for all timers |
| Main and Supervisor attempt conflicting assignments | Runtime accepts only the current owner/generation | Two active controllers mutating the same scope |
| Startup advances through genuine loading stages | Continue appropriate waiting or record a justified soft extension | Healthy work cancelled by a short observation timer |
| Heartbeats continue but useful progress stops | Investigate against the inactivity policy and change strategy/escalate | Unlimited waiting because the process is alive |
| Mutation response is lost after execution | Reconcile the original operation and avoid duplicate effects | Blind retry using a fresh identity |
| Read-only status request times out | Retry/observe appropriately without inventing an execution failure | Observation counted as a failed job |
| Input changes and the same validation command is needed again | Permit a justified rerun with current authority and retained history | Permanent duplicate ban based only on command text |
| Input is unchanged and the same failure repeats | Stop the unchanged strategy or escalate | Counters reset by rephrasing or handoff |
| Controller exits with a worker still active | Preserve identity, fence conflicting mutations and reconcile/clean up | Controller death treated as proof of worker death |
| Model claims completion but required files/checks are absent | Keep the task unverified | Narrative accepted as delivery |
| Supervisor reports success without evidence | Main rejects handback and retains the incident | Automatic de-escalation on a success statement |
| Verified handback succeeds | Main accepts ownership and resumes; temporary supervision ends | Supervisor remains active or routine work is lost |
| Same incident returns after handback | Reopen its history with the new evidence and reassess | New blank incident or recursive supervisor chain |
| Platform cannot switch models or launch workers | Honest single-agent fallback and explicit metadata limitations | Simulated independent review or fabricated model identity |
| Hard resource boundary is reached | Checkpoint and follow cancellation/cleanup policy | Silent renewal or unchecked execution |

## Measure useful outcomes

- **Verified completion rate:** tasks that meet the actual end-to-end acceptance criteria divided by tasks attempted. Keep unresolved, failed and cancelled outcomes visible.
- **Recurrence:** resolved incidents that recur with the same underlying cause. Match causes carefully; a repeated surface error may have a different cause.
- **Blocked time:** elapsed time from a substantiated blocker until verified resolution, distinguishing useful investigation from idle waiting.
- **Resource use per resolved issue:** tokens, calls, money, compute and elapsed time under clearly stated accounting boundaries.
- **Duplicate effects:** repeated external mutations that should have represented one logical operation.
- **False stalls:** healthy work stopped because an observation or inactivity rule was misapplied.
- **Unnecessary escalations:** cases handled by Supervisor where routine correction would have sufficed.
- **Handback quality:** handbacks accepted with complete evidence and a usable continuation state.
- **Scope discipline:** out-of-scope findings reported versus acted on without a new contract; record unnecessary work after the blocker was verified.
- **Time to handback:** elapsed time from verified blocker resolution to accepted transfer, separating required reconciliation from unrelated investigation.
- **Continuation after handback:** whether Main resumes the already-authorized next step without user prompting and the Supervisor issues no further work until reassigned.

A small example is not a benchmark. Compare similar tasks, include unsuccessful outcomes, report the model/effort actually used where observable, and preserve raw receipts privately where appropriate. Publish only sanitized evidence you are authorized to share.

## Comparative evaluation plan

Compare four candidate configurations:

1. One capable agent with tools and the same acceptance checks.
2. A conventional manager with bounded workers and verification.
3. Main and workers with temporary Supervisor escalation and accepted handback.
4. An always-active stronger coordinator with the same available specialists.

Use identical starting snapshots, tool access, acceptance criteria, and comparable total resource ceilings. State whether capability selection is held constant or changes between conditions; otherwise a gain from a stronger model could be misattributed to orchestration. Include orchestration, handoff, review, and failed-attempt costs.

Cover routine tasks, known difficult tasks, recurring cross-component failures, uncertain mutation delivery, healthy long-running operations, changed-input rereads, direct blocker dependencies, and later dependencies or unrelated findings that must be returned to Main. Include a resolved blocker with several tempting unrelated defects and an unavailable handback recipient. Repeat stochastic runs where feasible, report variability and unresolved outcomes, and reserve unseen tasks when tuning escalation rules. Distinguish an orchestration error from an unavailable capability or external service.

Add ablations when useful: the same recovery discipline without a separate Supervisor, and temporary supervision without independent acceptance checks. This helps identify whether value comes from the stronger reasoning, explicit evidence discipline, or transfer policy. Avoid broad superiority claims from a small selected demonstration.

## Current evidence

The [field observation](FIELD-OBSERVATION.md) documents selected local corrections in one private workflow. It is motivation for these scenarios, not a completed comparative evaluation. The checklist and plan on this page do not imply that an implementation has passed them.
