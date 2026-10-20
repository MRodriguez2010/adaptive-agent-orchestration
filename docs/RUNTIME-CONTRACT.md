# Runtime contract

The prompt describes desired behavior. The host application must provide enforcement for the guarantees below. This document is an implementation contract, not a supplied orchestration engine.

## Authoritative state

Maintain a durable record for each affected scope. A minimal record contains:

```json
{
  "task_id": "example-task",
  "scope_id": "example-scope",
  "incident_id": "example-incident",
  "active_orchestrator": "main",
  "control_generation": 1,
  "state": "running",
  "acceptance_criteria": [],
  "in_flight_operations": [],
  "evidence_references": [],
  "attempt_history": [],
  "budget_decisions": [],
  "next_step": "Continue the assigned work"
}
```

These identifiers are illustrative. The record must not hold credentials or treat a free-text claim as verified evidence.

## Assignment lifecycle

Bind each worker contract to its owner, control generation, objective, allowed resources, acceptance criteria, operation identities, and resource limits. A contract ending requires observed acceptance and reconciliation of its live operations, or an explicit transfer of those operations to another current assignment. Invalidate the completed assignment's authority at the assignment and mutation boundary; retaining the agent's session must not keep that authority active.

Ending authority does not prove process death, reverse an external side effect, or erase the contract's history. Retain late results as evidence and reconcile them against the current source and owner before acceptance. A new assignment must declare fresh authority without resetting the task's existing resource accounting.

An execution-mode change under the same owner preserves the task and operation records. A mode change that transfers ownership must also satisfy the atomic transfer rules below. Related findings outside the current authority remain findings until an authorized contract covers their correction.

For a Supervisor contract, store explicit scope exclusions, blocker acceptance checks, the return condition and a finite handback limit. Record incidental findings separately from work admitted to that contract. Accept an added dependency only with evidence that it prevents the declared blocker checks or safe handback and is already authorized; do not permit the Supervisor to expand its own scope or replace the completion criteria. A dependency of later Main work requires Main's separate disposition.

When blocker verification and owned-operation reconciliation pass, move the assignment to `handback_pending`. In that state, allow only bounded handback communication and necessary safety actions on already-owned operations; reject new investigations, assignments or unrelated mutations. Unrelated findings cannot veto blocker acceptance. At the declared handback limit, checkpoint and follow the safe fallback without fabricating a transfer or starting another investigation.

On accepted atomic transfer, close the Supervisor assignment, revoke its assignment/mutation authority and mark it inactive. Fence stale work even if the session or process remains available. Schedule or deliver Main's next already-authorized step through the host's real continuation mechanism, with one current owner and without another user "continue" request. Make that continuation recoverable without duplicate dispatch if delivery is uncertain. Record observed deactivation/continuation separately from intended behavior; a host lacking these mechanisms must report that limitation. A later Supervisor activation requires a new scoped assignment, with prior incident history and resource use retained.

## Atomic control transfer

A takeover or handback uses a compare-and-set transaction against the expected owner and generation. The update records its reason, evidence, accepted packet and new owner, then advances the generation. Reject stale transfers.

Check current ownership and generation at the mutation/assignment boundary. If external systems cannot enforce that check, serialize their access through a controlled adapter. Expiring a control lease may prevent new writes, but it does not kill an already-dispatched external action or prove its absence.

The outgoing orchestrator stops issuing affected assignments. Existing workers must either finish under an explicitly reconciled operation identity, checkpoint, or cancel through their real runtime. A takeover must not silently replay them.

## Durable operations and uncertain delivery

Persist operation intent before dispatch. Bind the operation to its task, scope, input/source identity, authority, and attempt. Retain dispatch and completion receipts separately.

When a response is lost:

1. Keep the original operation identity and mark the outcome unknown.
2. Query the executor or service's authoritative state.
3. Recover a verified result when present; otherwise establish whether execution is still active or safely absent.
4. Retry only when the action is idempotent, the executor deduplicates the operation, or reconciliation and current authority make a new attempt safe.

An HTTP timeout cannot establish non-execution. An engine's completed state cannot substitute for a missing application result when the acceptance contract requires that result. Cancellation acceptance also does not prove process death or reversal of an external side effect.

## Budgets and cleanup

Store concrete finite budgets before execution, including operation retry allowances and a bounded supervisory recovery phase within the overall task ceiling. Null example configuration values require selection before use. Report which controls are actually enforced; model-selected advisory limits must not be presented as runtime guarantees. Keep attempts and aggregate use across owner, worker, model and strategy changes.

Enforce hard resource ceilings and permissions outside the model. Allow soft budgets to change through recorded, authorized decisions with a future milestone and an upper bound. Never treat model commentary as renewal of a lease or execution grant.

A soft threshold expiring initiates evidence-based review. Preserve whether the operation is healthy, stalled, failed or unknown independently of the budget event. An authorized adjustment must remain within the finite task ceiling. At a hard boundary, block new dispatches and follow the declared reconciliation and cleanup reserve policy; record budget exhaustion without fabricating an execution or validation failure.

Track observation requests separately from execution attempts. Persist attempt counters and incident history across handoffs. Record any additional authority as a new explicit decision rather than editing historical failures or quietly resetting usage.

For process-based work, define who owns cancellation and how actual cleanup is observed. Controller exit, a stop request, and a confirmed empty execution scope are different facts. For external services, record any accepted side effect that remains after cancellation.

## Result acceptance

Validate result ownership, current applicability, expected source/input identity, declared checks, saved artifacts, and the evidence required for the task. A late result from an earlier generation may be retained and evaluated; it cannot issue current assignments or overwrite newer accepted state without an explicit reconciliation decision.

Keep claimed and observed metadata distinct. Store the actual model and effort when the provider exposes them. A requested selection alone must be labeled requested/unconfirmed.

## Pseudocode sketch

```text
on_event(event):
    record = durable_state.read(event.scope)
    classify event using executor evidence, not narrative alone

    if hard limits or required permissions prevent further work:
        block new dispatches
        reconcile/checkpoint using the declared cleanup/reserve policy
    else if result delivery is uncertain:
        reconcile the existing operation; do not redispatch automatically
    else if an ordinary correctable failure has a justified correction:
        assign a bounded correction under the current owner
    else if an escalation trigger is established:
        reconcile in-flight work
        atomically transfer affected scope to Supervisor
    else if progress supports an authorized soft-budget extension:
        persist the extension and next milestone before applying it

on_handback(packet):
    require current Supervisor ownership
    Main checks blocker acceptance and live-operation state
    record deferred findings without widening blocker acceptance
    reject only for a failed blocker criterion, missing required evidence,
        or unreconciled owned operation
    atomically transfer affected scope to Main
    close Supervisor contract and revoke its authority
    leave Supervisor inactive until a new scoped assignment
    deliver Main's next already-authorized step through the host
    reconcile uncertain continuation delivery before retrying
```

This sketch omits transport, storage and provider details. Implement and evaluate the actual adapters before claiming these guarantees.
