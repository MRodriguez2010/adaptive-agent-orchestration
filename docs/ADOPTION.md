# Apply the policy

## Any chat-based LLM

Copy the prompt at the very top of the [README](../README.md), or copy [the plain-text prompt](../prompts/global-orchestration.txt), into your assistant.

For persistent use, place it in the provider's supported custom-instructions, workspace-instructions or organization-policy feature. Respect the platform's instruction hierarchy. A normal chat message generally applies to that conversation; it must not be described as a persistent global configuration change without verification.

If a feature has a shorter instruction limit, retain the roles, exclusive ownership, evidence-based escalation, progress-aware waiting, safe retry rules, and verified handback. Link to or attach the complete policy where supported.

## Coding agents

Use the coding tool's documented user-level/global instruction mechanism when you want the policy across projects. Use a repository instruction file when you want it only in that repository. Common repository filenames include AGENTS.md, CLAUDE.md or GEMINI.md, but tools differ in which files they read and how they resolve precedence. Check the tool's documentation before choosing a location.

Merge with existing instructions. Do not replace permissions, credential handling, deployment rules or task-specific acceptance criteria. This repository intentionally does not include an automatically active repository instruction file: reading or cloning a guide should not silently change agent behavior.

## Multi-agent applications

Map the Main, Supervisor and Worker roles to available agents/models. Configure the allowed reasoning range and the scope of takeover. Install a runtime ownership record, operation ledger, result acceptance and resource enforcement following the [runtime contract](RUNTIME-CONTRACT.md).

Begin with Main and one worker only when delegation helps. Add independent workers when there is a clear benefit. A temporary Supervisor may coordinate those workers without adding another hierarchy of supervisors.

Treat worker assignments as bounded contracts. Close accepted assignments and release their authority after reconciling live operations. Use [execution modes](EXECUTION-MODES.md) to adapt the workflow without adding another permanent control layer. Prototype and compare the configurations in the [evaluation plan](EVALUATION.md) before making performance claims.

Use the [Supervisor assignment](../templates/supervisor-assignment.md) to fix the blocker scope, exclusions, acceptance checks and return condition before takeover. Direct dependencies must prevent that blocker's verification or safe handback to stay in scope; later Main work remains Main's decision. Do not let deferred findings extend the phase or prevent acceptance. After verified handback, revoke the completed assignment's authority and leave the Supervisor inactive until a new scoped assignment.

Connect accepted handback to Main's continuation in the actual host. Main must resume already-authorized work without requiring the user to say "continue." Verify that the Supervisor has stopped issuing work and Main can make the next authorized step. An idle retained session must not continue searching, polling or assigning. If the platform cannot activate the recipient automatically, report that capability limit and preserve the exact next action; a prompt cannot supply a missing scheduler or prove another model resumed.

Review [config/policy.example.yaml](../config/policy.example.yaml). Its null resource values are deliberate placeholders, not unlimited budgets. Before unattended execution, the host/operator must establish concrete finite limits and enforcement. An assistant may select and record generous task-appropriate starting limits within existing authority when values are absent; it cannot create runtime enforcement or silently relax a user-set hard limit. The file is a portable example, not a runnable configuration for an existing framework.

Separate observation timeouts, execution allowances, inactivity thresholds, retry budgets, supervisory recovery and the overall task ceiling. A short poll ending is a reason to inspect status, not to fail or restart healthy work. Permit recorded soft-limit adjustments when evidence supports them, while keeping finite overall resources and bounded recovery. Exhausted retries stop the unchanged strategy; supervision must also have a milestone and an end condition. Confirm these behaviors with the [evaluation scenarios](EVALUATION.md).

## Single-agent environments

Apply the triage, context, evidence, budget and verification rules within the one available agent. It can change approach or request a user decision when necessary. It must not claim that a different model, independent reviewer or worker executed when no such capability exists.

## Confirm adoption

Ask the assistant to report the applied scope, roles, actual available models/tools, escalation triggers, enforced versus cooperative ownership, resource boundaries, and handback requirements. Then exercise the [evaluation scenarios](EVALUATION.md).

Treat this as a policy to validate against your workload. It does not guarantee that an LLM follows every instruction, that a stronger model solves every blocker, or that external operations become exactly-once.
