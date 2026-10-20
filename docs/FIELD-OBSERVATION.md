# Field observation: temporary supervision during a repair

## Evidence status

This is a sanitized observation from one private software-repair workflow, reviewed on 19 October 2026. The project owner reported that a temporary stronger-reasoning Supervisor found and helped resolve issues that were not all blocking the immediate step but could affect later progress.

The reviewed material consists of coordinator and Supervisor session records containing findings, review decisions, and reported validation results. Private identifiers, provider/model mapping, paths, operational logs, and deployment details are omitted. Readers cannot independently reproduce the private run from this page. The underlying product checks were not rerun as part of preparing this report.

## What the reviewed records support

| Finding or intervention | Recorded local outcome | Limit on the inference |
|---|---|---|
| A delayed claim replay could give a worker more execution time than remained on the original authority. | Supervisor reported an offline reproduction, directed a focused correction, and accepted the source after focused checks. | This supports a specific lease-boundary correction, not the resolution of every earlier failure. |
| Progress handling could reject a repeated read even after the underlying file changed. | Reviewed source allowed rereading after a verified content change; focused checks were reported as passing. | The policy still needs to stop unchanged failing strategies. |
| A lost claim response followed by a rejection could erase the earlier uncertainty. | Review identified the additional edge case before integration and accepted a correction preserving uncertainty across later errors. | The earlier side effect still requires reconciliation; a later rejection is not proof of non-execution. |
| Failed installation diagnostics could be lost during rollback. | A separate, bounded logging correction retained error evidence before rollback; offline checks were reported as passing. | Diagnostic retention does not establish installation success. |
| A coordination guard had incident-identity and audit-history gaps. | Supervisor caught the gaps before use, requested correction, and later admitted a bounded assignment through the guard. | Direct native collaboration calls remained outside the guard's enforcement boundary. |

The records support targeted findings, delegated corrections, and local source acceptance. They do not establish that every finding originated with the Supervisor or that the overall project was completed. Later installation and capacity checks still produced blockers. A completed return of overall control to Main was not established in the reviewed snapshot.

## What the experience suggests

The owner reported value from reviewing related failure paths before later steps depended on them. A reasonable hypothesis is that bounded supervisory review can discover additional defects while the relevant context is available. The workflow also illustrates why source acceptance, package preparation, successful installation, and end-to-end completion must remain separate states.

Whether these interventions prevented later delays is a counterfactual. No paired baseline, controlled comparison, quantified time saving, or general performance advantage is available. This observation does not demonstrate superiority over Magentic-One, a conventional manager–worker system, or one capable agent.

## Owner-reported scope drift after resolution

In a subsequent owner report, the Supervisor remained active after solving its assigned issue because it continued finding other issues outside the main request. The owner requested a clear end: deliver the assigned solution and evidence, list other findings without taking them on, return control to Main, and become inactive until needed again.

This follow-up is an owner-reported failure mode, not an independently reproduced execution trace or a measured estimate of wasted time. It qualifies the earlier hypothesis about useful preventive review: discovering a defect does not make its correction part of the current contract. The updated policy requires direct necessity for the assigned blocker, accepts deferred findings without extending supervision, and specifies inactive supervision plus Main's continuation after accepted handback. These are policy requirements to evaluate; updating this guide does not prove a host enforces them.

## Turning the observation into stronger evidence

Use synthetic or authorized publishable fixtures for delayed delivery, expiring authority, changed-input rereads, lost diagnostics, and stale assignments. Compare the same task and capability pool with and without temporary supervision, under comparable resource ceilings. Preserve failures as well as successes and measure accepted completion, recurrence, duplicate effects, elapsed time, and resource use.

See the [evaluation plan](EVALUATION.md). Any future claim that this policy improves outcomes should identify the implementation, task set, baseline, and evidence boundary.
