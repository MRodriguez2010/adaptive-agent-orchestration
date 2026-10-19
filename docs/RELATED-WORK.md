# Related work, attribution, and contribution

## What this project contributes

[MRodriguez2010](https://github.com/MRodriguez2010) developed and documented **Contract Orchestration: Adaptive Agents** as a practical policy and adoption kit. Its particular design combines:

- A stable Main coordinator for user continuity.
- Bounded specialist assignments for difficult work and blockers.
- Temporary Supervisor ownership of the affected plan and workers when escalation is justified.
- One active authority per affected scope, with stale-assignment rejection as a runtime requirement.
- Progress-aware waiting, safe reconciliation, and retained operation and incident history.
- Acceptance evidence, explicit handback, and release of temporary responsibilities.

Credit for this project's policy text, templates, diagram, and evaluation design is appropriate. The project does not claim the first invention of these ingredients, an unprecedented combination, an implemented general-purpose engine, or superior task performance. Its previous title, *Adaptive Agent Orchestration*, used terminology that already appears in other work.

The links below distinguish established concepts and related projects from this project's choices. Discovery during this review does not imply that a source influenced the earlier draft. References do not imply endorsement, affiliation, implementation compatibility, or reproduction of the cited results.

## Core patterns and historical context

| Primary source | Established idea | Relationship to this guide |
|---|---|---|
| [Reid G. Smith, Contract Net Protocol, 1980](https://reidgsmith.com/The_Contract_Net_Protocol_Dec-1980.pdf) | Task allocation through announcements, negotiation, bids, and contract awards. | Task contracts are established multi-agent terminology. Here, a contract specifies bounded responsibility and acceptance; no negotiation or bidding mechanism is supplied. |
| [OpenAI, orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration) | A manager can retain the user-facing answer while using specialists, or transfer a branch to a specialist. | Main retains user continuity; Supervisor takeover transfers the affected operational scope. A normal specialist call is not automatically a transfer of orchestration authority. |
| [Anthropic, building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Chaining, routing, parallelization, orchestrator–workers, and evaluator–optimizer patterns. | These are reusable execution patterns beneath this policy. Bounded delegation and evaluation are established ideas. |
| [Microsoft, Magentic-One architecture](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html#architecture), [2024 paper](https://arxiv.org/abs/2411.04468) | An orchestrator uses task and progress ledgers, directs specialists, and replans after inadequate progress. The documentation also describes experiments with different models in the outer planning loop. | A close adaptive-recovery precedent. This guide emphasizes temporary scoped takeover, explicit authority transfer, and accepted handback; it does not claim those choices are unprecedented. |
| [Microsoft, AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | Sequential, concurrent, group chat, handoff, and Magentic patterns, with task-specific tradeoffs. | Provides broader pattern vocabulary. There is no single universal winner for complex work. |
| [LangGraph, workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Explicit workflow transitions and persistent graph state support continuation and recovery. | Potential implementation building blocks. Persistence alone does not establish exclusive authority, deduplicated external mutations, or this guide's full runtime contract. |

## Closest public policy projects

| Project | Relevant overlap | Boundary of this comparison |
|---|---|---|
| [YuemingHub, Adaptive Agent Orchestration Protocol](https://github.com/YuemingHub/Adaptive-Agent-Orchestration-Protocol) | Host-independent project understanding, routing, bounded teams, verification, and replanning. Its [initial August 2026 README](https://github.com/YuemingHub/Adaptive-Agent-Orchestration-Protocol/blob/1cdebed0843c0c460197c0722cb1d880aeb5874c/README.md) already used the similar name. | Earlier naming and conceptual overlap are acknowledged. This is not a security, compatibility, production-readiness, or comparative-performance assessment of that project. |
| [VAMFI, Dynamic Workflows for Codex](https://github.com/VAMFI/dynamic-workflows-for-codex) | A portable instruction policy and evaluation kit for minimal useful delegation, root integration, and verification. Its [July 2026 revision](https://github.com/VAMFI/dynamic-workflows-for-codex/tree/ee94e368ced6fad30d82972775897b4e999bfd74) predates this guide. | A close example of the policy-kit format. No performance ranking or code reuse is asserted. |

## Selecting or revising orchestration

| Research | What it investigates | What should not be inferred |
|---|---|---|
| [Yue et al., MasRouter, ACL 2025](https://aclanthology.org/2025.acl-long.757/) | Selecting collaboration modes, agent roles, and language models through a routing controller. | Model routing and team-structure selection do not by themselves establish safe transfer of live execution authority. |
| [Wang et al., TROVE, September 2026 preprint](https://arxiv.org/abs/2609.05019) | Revising provisional execution routes when runtime evidence invalidates a continuation, including local correction and suffix replacement. | Reported benchmark results do not demonstrate safe arbitrary switching between unrelated live runtimes. |
| [Hu, Lu, and Clune, Automated Design of Agentic Systems, 2024](https://arxiv.org/abs/2408.08435) | A meta-agent searches for agent-system designs represented in code. | Searching and evaluating designs is different from recovering an ongoing task by switching its execution mode. |
| [Kim et al., Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296), revised April 2026 | Controlled comparisons show that coordination effects depend on task structure, model capability, and overhead. | More agents or a more elaborate hierarchy do not establish better performance. The study does not evaluate this project. |

These sources establish precedent for a controller choosing or revising orchestration. This guide recommends [bounded execution modes](EXECUTION-MODES.md) under stable authority and state before adding another permanent supervisory layer.

## Codex and platform capabilities

[OpenAI's description of the Codex harness](https://developers.openai.com/blog/codex-as-a-platform) explains the execution system around the model, including tools, state, and configured boundaries. [OpenAI's Responses multi-agent documentation](https://developers.openai.com/api/docs/guides/responses-multi-agent) describes a root agent delegating to subagents and synthesizing results. The API documentation is a specific capability reference, not a complete account of every Codex surface's internals.

Neither reference establishes that every installation automatically implements this guide's stronger-supervisor takeover, fencing, operation reconciliation, and verified handback. Adoption must report what is actually supported and enforced. Reading this repository is not installation.

## Attribution and public claims

A suitable project description is: **a policy and adoption kit developed by MRodriguez2010 that combines established orchestration patterns with bounded temporary assignments, scoped supervisor escalation, and evidence-based handback.** Cite the repository and the revision discussed when describing its particular design. Preserve the existing MIT notices when reusing its material; this citation suggestion adds no license restriction.

Avoid claims that this project invented adaptive orchestration, originated task contracts, guarantees correct execution through a prompt, or outperforms existing systems. The [field observation](FIELD-OBSERVATION.md) supports motivation and selected local outcomes. The [evaluation plan](EVALUATION.md) describes what stronger comparative evidence would require.
