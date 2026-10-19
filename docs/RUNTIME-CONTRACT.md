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

Enforce hard resource ceilings and permissions outside the model. Allow soft budgets to change through recorded, authorized decisions with a future milestone and an upper bound. Never treat model commentary as renewal of a lease or execution grant.

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

    if result delivery is uncertain:
        reconcile the existing operation; do not redispatch automatically
    else if an ordinary correctable failure has a justified correction:
        assign a bounded correction under the current owner
    else if an escalation trigger is established:
        reconcile in-flight work
        atomically transfer affected scope to Supervisor
    else if progress supports an authorized soft-budget extension:
        persist the extension and next milestone before applying it
    else if hard limits or required permissions prevent further work:
        checkpoint and perform the declared cleanup/escalation

on_handback(packet):
    require current Supervisor ownership
    Main checks blocker acceptance and live-operation state
    atomically transfer affected scope to Main
    Main resumes remaining work
```

This sketch omits transport, storage and provider details. Implement and evaluate the actual adapters before claiming these guarantees.
