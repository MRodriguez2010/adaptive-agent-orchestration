# Graph and text alternative

[Full-size SVG](../assets/orchestration.svg) · [PNG export](../assets/orchestration.png) · [Mermaid source](orchestration.mmd) · [Layout source](../tools/build_diagram.py)

Main normally controls the work. A blocked or recurring issue triggers temporary Supervisor ownership. The Supervisor resolves the blocker, provides verification evidence and offers handback. Main checks that evidence and accepts control before normal work resumes.

Both roles connect to one runtime ownership gate. That gate permits only the current orchestrator to assign or mutate the affected scope. It delegates to the smallest useful set of implementation, investigation or verification workers; the illustrated worker roles are examples, not a mandatory three-agent team.

Workers return observed outputs, checks and operation state to durable evidence. That evidence is available to whichever role currently owns the affected scope. Solid paths show work/control and handback. The dashed path highlights temporary Supervisor control. Gray paths carry evidence and live status.

The runtime always enforces permissions, resource ceilings, cancellation/cleanup and result acceptance. Startup, execution and inactivity budgets can adapt to justified evidence. A short status-request timeout does not establish execution failure.

The SVG and Mermaid graph are generated from the same layout script. Mermaid gives an editable portable topology; its automatic layout may differ from the SVG's arranged layout. PNG is a convenience export.

Regenerate the SVG and Mermaid source:

```sh
python3 tools/build_diagram.py
```

Also regenerate the PNG when Python Cairo and librsvg bindings are installed:

```sh
python3 tools/build_diagram.py --png
```
