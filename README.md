```text
Apply this contract-based adaptive orchestration policy to my work at the broadest supported
instruction scope I have authorized. Preserve higher-priority instructions, existing
permissions, active operations, data, and resource constraints. If you cannot persist
global settings, apply it to this conversation and explain exactly where I can save it;
never claim a global change you did not make.

ROLES
Use a capable Main model as the normal coordinator and user interface. Delegate only
when specialization, independent work, or context isolation materially helps. Keep the
smallest useful team. Give each worker a clear objective, allowed scope, acceptance
criteria, evidence requirements, and stopping conditions. Record the actual model and
reasoning effort used when the platform exposes them; otherwise mark them unconfirmed.

Treat each specialist assignment as a bounded operational contract: objective, inputs,
scope, authority, acceptance evidence, resources, and an end condition. Bring in temporary
specialists for difficult work or blockers when their capability materially helps; a
failed attempt is not a prerequisite. After accepted delivery, reconcile live operations
and release the assignment's authority. Reuse an idle worker only under a new assignment.

TEMPORARY SUPERVISOR
Blocked work, recurring failures after meaningful corrections, contradictory
cross-component evidence, or uncertainty about execution ownership/delivery should
trigger a stronger-reasoning Supervisor. Choose effort appropriate to the blocker, up to
the highest supported level when justified. Do not require every timer or retry counter
to expire first. Ordinary correctable tool or test failures can remain with the assigned
worker.

The Supervisor temporarily owns the blocker-resolution plan, affected worker
assignments, coordination, and synthesis. Main remains the user-facing coordinator and
may continue genuinely independent work. Exactly one orchestrator may issue assignments
or approve mutations for the affected scope. Transfer control at a safe boundary,
reconcile in-flight operations, and prevent stale or conflicting assignments. Do not add
recursive layers of supervisors.

Triage related defects found during investigation. Correct one within existing authority
when evidence links it to the current acceptance criteria or a required next dependency.
Otherwise retain the finding, likely impact and proposed follow-up for Main. Do not turn
preventive review into unlimited cleanup or claim that a future failure was prevented
without evidence.

HANDOFF
Provide a compact, authoritative packet: objective and acceptance criteria; current
source/state and evidence links; exact failures and attempted corrections; hypotheses
established or ruled out; in-flight operation identities; permissions, ownership, and
remaining resource budget. Preserve access to original evidence without requiring a
reconstruction of the entire conversation.

WAITING AND RECOVERY
Distinguish healthy progress, observation/transport timeouts, genuine stalls, failed
validation, and policy denials. Use separate startup, execution, inactivity, and overall
resource budgets appropriate to the task. A short observation timeout ends that
observation; it does not establish that the underlying operation failed. Reconcile
uncertain delivery before retrying a possibly executed action.

Continue waiting or extend a soft budget when evidence supports progress, with a
recorded reason and a next observable milestone. A heartbeat proves liveness, not useful
progress. Repeated explanations or status messages alone are not progress. Keep
externally enforced permission boundaries, acceptance criteria, resource ceilings, and
cancellation/cleanup requirements intact. Do not silently renew expired execution
authority or make an old failure appear successful.

Retry only when safe: a transient failure is confirmed, or new evidence, corrected
input, changed state, or an implementation change justifies another attempt. Use
operation identities and deduplication for side effects where available. Repeating a
read-only observation may be appropriate; repeating an uncertain mutation requires
reconciliation. Stop an unchanged failing strategy, preserve evidence, and change
approach or escalate.

VERIFICATION AND HANDBACK
Resolve the blocker against its stated acceptance criteria using inspectable results,
actual checks, and appropriate independent verification. Then return to Main with the
root cause, exact changes, validation evidence, limitations, live-worker/in-flight
state, and the next concrete step. Main checks the handback, explicitly accepts control,
and resumes the task. End the temporary supervisory phase. If the same blocker returns,
reopen its incident with new evidence rather than resetting history or creating another
supervisory layer.

CONTINUITY AND HONEST STATUS
Keep one durable task/incident record containing ownership, state, evidence, attempts,
budget decisions, and the next step. Distinguish planned, dispatched, running,
execution-unknown, failed, cancelled, verified, and complete. A model's success claim,
heartbeat, or dispatch acknowledgment is not proof of completion. Runtime mechanisms
must enforce exclusive ownership, permissions, durable operations, and deduplication;
prompt instructions alone cannot guarantee them.

If multiple agents or model switching are unavailable, state that limitation and apply
the same planning, triage, verification, and evidence discipline in a single-agent
workflow. Never simulate an independent reviewer or claim another model ran. Continue
autonomously within authorized scope; ask me only for a missing decision, required
access, or a material change in scope or resources. Track verified completion, recurring
blockers, blocked time, and resource use per resolved issue.
```

# Contract Orchestration: Adaptive Agents

A practical, model-agnostic policy for bounded specialist assignments, temporary supervisor takeover, progress-aware recovery, and verified handback.

Developed and documented by [MRodriguez2010](https://github.com/MRodriguez2010). The contribution is this particular policy, its assignment and handback contracts, reusable templates, diagram, and evaluation scenarios. It combines established orchestration ideas; it makes no claim to have invented adaptive orchestration, task contracts, supervisors, or verified delegation. See [related work and attribution](docs/RELATED-WORK.md).

**Status:** documented policy and adoption kit. There is no supplied orchestration engine or controlled evidence of superiority. A [sanitized field observation](docs/FIELD-OBSERVATION.md) records useful local corrections during one supervised repair, with its verification and publication limits.

Here, a **contract** is an operational assignment with an objective, bounded authority, acceptance evidence, and an explicit end. Temporary specialists handle difficult work or blockers, deliver evidence, and leave the assignment after acceptance. Main keeps user continuity. A specialist who only supplies advice remains a worker; a Supervisor receives temporary control over the affected workers and plan.

The project was previously titled *Adaptive Agent Orchestration*. The new title describes its focus more precisely; it is not a claim that the underlying concepts are new.

**Start here:** copy the prompt above into your preferred LLM. For persistence, save it through that tool's supported global/custom-instruction mechanism. A pasted message alone does not prove a global setting changed. The same prompt is available as [plain text](prompts/global-orchestration.txt).

![Orchestration node graph: Main and a temporary Supervisor share one runtime-enforced ownership gate; workers return evidence; verified handback restores Main control.](https://raw.githubusercontent.com/MRodriguez2010/contract-orchestration-adaptive-agents/4b9fc20652b4474267dae9581ffa2b7b6d7d5b10/assets/orchestration.png)

[Full-size PNG](assets/orchestration.png) · [Editable SVG](assets/orchestration.svg) · [Mermaid source](diagrams/orchestration.mmd) · [Text alternative](diagrams/README.md)

## How it works

1. **Main coordinates normal work.** It maintains continuity, delegates only when useful, and remains the user interface.
2. **Bounded contracts bring in specialists.** Difficult work may justify a temporary specialist before a failure. A recurring blocker, contradictory state, or unresolved execution ambiguity can justify Supervisor takeover before arbitrary counters expire.
3. **Supervisor takes temporary control.** It owns the affected plan and workers. Exactly one orchestrator controls that scope.
4. **Waiting and recovery adapt to progress.** Observation timeouts, actual failed tests, healthy execution and genuine stalls receive different treatment.
5. **Verification precedes handback.** Supervisor returns the cause, change, evidence, limitations and continuation state. Main reviews and accepts control.
6. **Temporary responsibilities end.** Accepted assignments release their authority after live operations are reconciled. Main resumes remaining work. Recurring incidents retain their history.

## Read and reuse

| Resource | What it provides |
|---|---|
| [Orchestration policy](docs/ORCHESTRATION.md) | Roles, escalation, ownership transfer, limits, recovery, verification and metrics |
| [Runtime contract](docs/RUNTIME-CONTRACT.md) | Atomic ownership, fencing, durable operations, uncertain delivery and result acceptance |
| [Adoption guide](docs/ADOPTION.md) | Chat, persistent instructions, coding agents, applications and single-agent fallback |
| [Evaluation scenarios](docs/EVALUATION.md) | Concrete expected behaviors and useful outcome metrics |
| [Related work and attribution](docs/RELATED-WORK.md) | Established patterns, closest projects, research references, and defensible contribution claims |
| [Execution modes](docs/EXECUTION-MODES.md) | Choose and change bounded workflows under one authority and state layer |
| [Field observation](docs/FIELD-OBSERVATION.md) | Sanitized experience, observed local corrections, and limits on evidence |
| [Handoff](templates/handoff.md) / [Handback](templates/handback.md) | Compact transfer packets with evidence and live-operation state |
| [Worker assignment](templates/worker-assignment.md) | Scope, ownership, acceptance, budgets and stopping conditions |
| [Budget decision](templates/budget-decision.md) | Reasons, authority, next milestones and retained attempt history |
| [Example policy](config/policy.example.yaml) | Provider-neutral configuration outline with operator-defined resource limits |

## What the prompt can and cannot do

The prompt can guide an assistant's planning, triage, delegation and reporting. Actual model switching and worker execution require those platform capabilities. Exclusive ownership, permissions, durable state, deduplication and hard resource ceilings require runtime enforcement. This repository is a documented policy and adoption kit; it does not include an orchestration engine or claim these mechanisms have been implemented for your platform.

A stronger model may improve difficult reasoning. It cannot make failed tests pass without a correction, infer missing execution evidence, or create permissions it has not been granted. Successful dispatch and healthy heartbeats also do not establish task completion.

## Diagram sources

The SVG is an editable vector export; the Mermaid file provides a portable logical graph. To regenerate the SVG from its layout source, run `python3 tools/build_diagram.py`. To regenerate the README's first prompt block after editing the plain-text prompt, run `python3 tools/sync_readme_prompt.py`.

The PNG is a convenience export. SVG generation uses Python's standard library. PNG export uses the optional system Python bindings for Cairo and librsvg; see the diagram tool's `--png` option.

## Design references and related work

The policy choices are recommendations to evaluate against your workload. These references establish context; they do not endorse or validate this project:

- [OpenAI: orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) distinguishes a manager retaining control from a specialist taking over a branch of work.
- [Anthropic: building effective agents](https://www.anthropic.com/engineering/building-effective-agents) describes orchestrator/worker workflows, incremental complexity and stopping conditions.
- [Microsoft: Magentic-One](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html#architecture) describes task and progress ledgers, specialist coordination, and replanning when progress stalls.
- [Reid G. Smith: Contract Net Protocol (1980)](https://reidgsmith.com/The_Contract_Net_Protocol_Dec-1980.pdf) establishes an earlier task-contract approach based on negotiation and awards. This guide does not specify a bidding protocol.
- [YuemingHub: Adaptive Agent Orchestration Protocol](https://github.com/YuemingHub/Adaptive-Agent-Orchestration-Protocol) and [VAMFI: Dynamic Workflows for Codex](https://github.com/VAMFI/dynamic-workflows-for-codex) are related public policy and workflow projects with overlapping terminology and goals.

The [full comparison](docs/RELATED-WORK.md) also covers Microsoft orchestration patterns, LangGraph, Codex's harness and multi-agent capabilities, MasRouter, TROVE, Automated Design of Agentic Systems, and research on agent-system scaling. Sources identified during the related-work review are described as related work, without retroactively claiming they inspired the original draft.

No particular provider, framework, model name or reasoning label is required.

## License

[MIT](LICENSE). Reuse and adapt the prompt, documentation, templates and diagrams.
