# Choose and change execution modes

Keep one authoritative task record and one active orchestrator per affected scope. Let the current owner choose the smallest useful execution mode. The recovery contract can apply across modes; it need not replace them.

| Task structure | Starting mode | Useful example | Main cost or limitation |
|---|---|---|---|
| Tightly coupled work with shared state | One agent using tools and feedback | Focused bug repair | One context can become overloaded. |
| Known dependent stages | Sequential pipeline with acceptance gates | Extract, validate, transform, then publish an approved artifact | An unexpected dependency may require replanning. |
| Independent bounded outputs | Parallel specialists, followed by synthesis | Compare hypotheses or inspect separate components | Communication and integration can outweigh the saved time. |
| Unknown decomposition across specialties | Manager and workers | Cross-component investigation | The manager must reconcile evidence and ownership. |
| A deliverable with a trustworthy evaluator | Implementation–verification loop | Repair code against meaningful checks | Weak acceptance criteria can produce endless revisions. |
| Discussion improves a decision | Bounded review or debate | Compare design proposals | Agreement is not evidence of correctness. |
| A blocker exceeds the current approach | Temporary Supervisor takeover | Recurring integration failure or unresolved execution ambiguity | Handoff costs, lost context, and competing control must be managed. |

These are selection guidelines, not measured performance claims. [Related work](RELATED-WORK.md) supplies the underlying patterns and research.

## Change mode at an observable boundary

1. Record the evidence that the current mode is insufficient and the expected benefit of changing it.
2. Identify accepted outputs, required next inputs, live operations, remaining authority, and resource ceilings.
3. Reconcile live work before assigning conflicting actions. Preserve existing operation identities and outcomes.
4. If the owner changes, apply the [runtime transfer contract](RUNTIME-CONTRACT.md). A mode change under the same owner does not itself require a takeover.
5. Declare the new bounded assignments, acceptance criteria, next observable milestone, and condition for stopping or switching again.
6. Evaluate the result. Retain the reason and cost of the change, including unsuccessful switches.

Do not switch modes to erase a failure, restart accounting, escape a permission boundary, or keep an unchanged failing strategy running. Frequent switching without useful progress is itself a reason to reassess.

## An evolving task

A feature starts as sequential implementation. An unfamiliar dependency creates two independent hypotheses, so the owner assigns bounded parallel investigations. The findings establish a shared-state defect, so one worker implements the correction and another performs a consequential check. If repeated meaningful corrections still fail, Main transfers the affected scope to a temporary Supervisor. After acceptance and reconciled operations, Supervisor hands back and its temporary authority ends.

This is adaptation within one task and authority model. Using several unrelated orchestration engines would additionally require tested state, operation, permission, and cancellation adapters. Add that complexity only when measured benefits justify it.

## Related findings and preventive work

A specialist may discover a defect that does not block the current step but threatens an identified later dependency. Record the finding, supporting evidence, affected dependency, likely consequence, and proposed check. Fix it within the current contract only when evidence shows it prevents the assigned acceptance checks or safe handback and the correction is already authorized. A dependency of later Main work does not extend the Supervisor's assignment. Return it to Main for a separately scoped decision.

Temporary responsibility ends after accepted delivery and operation reconciliation. An idle agent can be retained for reuse, but a new assignment must establish its current scope and authority. A saved session or live process does not grant continuing mutation rights.

Once the assigned blocker is verified, unrelated discoveries do not justify switching modes to continue supervision. Hand back the result and deferred findings, deactivate the Supervisor after acceptance, and let Main continue the authorized task. A later need for stronger diagnosis requires a new bounded assignment or an evidence-backed recurrence of the original incident.
