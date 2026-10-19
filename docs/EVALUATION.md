# Evaluate behavior before relying on it

These scenarios define expected behavior. They are a review checklist, not evidence that a runtime implementation has passed.

| Scenario | Expected behavior | Failure to detect |
|---|---|---|
| Routine task succeeds | Main completes and verifies without unnecessary supervision | Supervisor added to every task |
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

A small example is not a benchmark. Compare similar tasks, include unsuccessful outcomes, report the model/effort actually used where observable, and preserve raw receipts privately where appropriate. Publish only sanitized evidence you are authorized to share.
