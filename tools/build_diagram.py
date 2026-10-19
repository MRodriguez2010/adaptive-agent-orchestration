#!/usr/bin/env python3
"""Build the editable SVG and Mermaid graph. Optional PNG uses Cairo/librsvg."""
from pathlib import Path
from html import escape
import argparse

ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1600, 1380
NODES = [
    ('main', 'Main coordinator'), ('supervisor', 'Temporary supervisor'),
    ('owner', 'One active orchestrator'), ('build', 'Implementation'),
    ('investigate', 'Investigation'), ('verify', 'Verification'),
    ('evidence', 'Evidence and durable task state'),
]
EDGES = [
    ('main', 'supervisor', 'Blocked or recurring issue'),
    ('supervisor', 'main', 'Verified repair and accepted handback'),
    ('main', 'owner', 'Normal ownership'),
    ('supervisor', 'owner', 'Temporary ownership'),
    ('owner', 'build', 'Assign'), ('owner', 'investigate', 'Assign'),
    ('owner', 'verify', 'Assign'), ('build', 'evidence', 'Results'),
    ('investigate', 'evidence', 'Results'), ('verify', 'evidence', 'Results'),
    ('evidence', 'owner', 'Evidence and live status'),
]

def build_svg():
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title description">
<title id="title">Adaptive agent orchestration</title>
<desc id="description">Main coordinates routine work. A blocker or recurring issue transfers affected work to a temporary Supervisor. A runtime gate permits one active orchestrator per scope. Workers return observed results to durable evidence and the active owner. Verified repair and Main's accepted handback restore normal control. Permissions, resource ceilings, cancellation and acceptance remain enforced.</desc>
<defs>
  <marker id="arrow-blue" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L10 5 L0 10 Z" fill="#2864bd"/></marker>
  <marker id="arrow-orange" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L10 5 L0 10 Z" fill="#b75524"/></marker>
  <marker id="arrow-green" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L10 5 L0 10 Z" fill="#25725a"/></marker>
  <marker id="arrow-gray" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L10 5 L0 10 Z" fill="#728093"/></marker>
</defs>
<rect width="1600" height="1380" fill="#f6f8fb"/>
<g font-family="DejaVu Sans, Arial, sans-serif" fill="#182638">
''']
    def text(x, y, value, size=24, color='#182638', anchor='start', weight=400, extra=''):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{escape(value)}</text>')
    def rect(x, y, w, h, fill, stroke, radius=22):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    def path(edge, d, color, marker=None, dash=False, width=4):
        tail = (f' marker-end="url(#{marker})"' if marker else '') + (' stroke-dasharray="10 7"' if dash else '')
        parts.append(f'<path data-edge="{escape(edge)}" d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{tail}/>')
    def card(node, x, y, w, h, fill, stroke, heading, lines):
        parts.append(f'<g id="node-{node}" data-node="{node}">')
        rect(x, y, w, h, fill, stroke)
        text(x+w/2, y+48, heading, 30, anchor='middle', weight=600)
        for offset, value, size, color in lines:
            text(x+w/2, y+offset, value, size, color, 'middle')
        parts.append('</g>')

    text(96, 76, 'Adaptive agent orchestration', 48, weight=600)
    text(98, 120, 'Keep continuity. Escalate difficult work. Return with proof.', 25, '#536277')
    rect(140, 165, 220, 36, '#e8f0fc', '#e8f0fc', 10)
    text(156, 190, 'NORMAL OPERATION', 18, '#285b9c', weight=600)
    rect(1040, 165, 310, 36, '#fcebdc', '#fcebdc', 10)
    text(1056, 190, 'EVIDENCE-BASED ESCALATION', 18, '#9b4b24', weight=600)

    path('main-supervisor', 'M560 300 H1040', '#b75524', 'arrow-orange')
    text(800, 272, 'Blocked or recurring issue', 22, '#98451f', 'middle', 500)
    path('supervisor-main', 'M1040 370 H560', '#25725a', 'arrow-green')
    text(800, 410, 'Verified repair + accepted handback', 20, '#25644f', 'middle', 500)
    path('main-owner', 'M350 440 V490 Q350 510 370 510 H610 V540', '#2864bd', 'arrow-blue')
    path('supervisor-owner', 'M1250 440 V490 Q1250 510 1230 510 H990 V540', '#b75524', 'arrow-orange', True)
    text(370, 482, 'Routine control', 20, '#285b9c')
    text(1220, 482, 'Control during takeover', 20, '#98451f', 'end')
    path('owner-workers', 'M800 675 V725 M350 725 H1250', '#2864bd', width=4)
    path('owner-build', 'M350 725 V790', '#2864bd', 'arrow-blue')
    path('owner-investigate', 'M800 725 V790', '#2864bd', 'arrow-blue')
    path('owner-verify', 'M1250 725 V790', '#2864bd', 'arrow-blue')
    text(160, 708, 'Delegate only when useful.', 21, '#536277')
    text(1460, 708, 'Smallest useful team', 21, '#536277', 'end')
    path('build-evidence', 'M350 940 V995 H800', '#728093', width=3)
    path('investigate-evidence', 'M800 940 V1060', '#728093', 'arrow-gray', width=3)
    path('verify-evidence', 'M1250 940 V995 H800', '#728093', width=3)
    text(160, 1035, 'Observed outputs + checks + operation state', 21, '#536277')
    path('evidence-owner', 'M1080 1130 H1510 V620 H1040', '#728093', 'arrow-gray', width=3)
    text(1545, 875, 'Evidence and live status return to the active owner', 20, '#536277', 'middle', extra='transform="rotate(-90 1545 875)"')

    card('main', 140, 220, 420, 220, '#eaf2ff', '#aec7eb', 'Main coordinator', [
        (96, 'Routine planning and delivery', 23, '#285b9c'),
        (132, 'User interface + task continuity', 23, '#285b9c'),
        (182, 'Capable general model', 20, '#536277'),
    ])
    card('supervisor', 1040, 220, 420, 220, '#fff0e3', '#e4c1a3', 'Temporary supervisor', [
        (96, 'Owns the blocker-resolution plan', 22, '#98451f'),
        (132, 'Coordinates affected workers', 22, '#98451f'),
        (182, 'Stronger reasoning · up to maximum', 19, '#536277'),
    ])
    card('owner', 560, 540, 480, 135, '#eeeafa', '#c9bde8', 'One active orchestrator', [
        (83, 'Main OR Supervisor · one owner per scope', 20, '#584580'),
        (113, 'Reject stale or conflicting assignments', 20, '#584580'),
    ])
    for node, x, heading, detail in [
        ('build', 160, 'Implementation', 'Produce or change artifacts'),
        ('investigate', 610, 'Investigation', 'Test competing explanations'),
        ('verify', 1060, 'Verification', 'Check accepted outcomes'),
    ]:
        card(node, x, 790, 380, 150, '#ffffff', '#bfd8ce', heading, [
            (88, detail, 21, '#365e50'),
            (123, 'Worker · task-appropriate model', 19, '#536277'),
        ])
    card('evidence', 520, 1060, 560, 140, '#eaf0f5', '#c9d4e1', 'Evidence & durable task state', [
        (87, 'Results · attempts · budgets · next step', 22, '#46596e'),
        (119, 'Original failures + observed model identity', 20, '#536277'),
    ])
    rect(140, 1250, 1320, 60, '#ffffff', '#dce3ed', 16)
    text(800, 1288, 'Always enforced: permissions · resource ceilings · safe cancellation · acceptance evidence', 22, '#46596e', 'middle')
    text(800, 1345, 'Adapt startup, execution and inactivity budgets to evidence. A short poll timeout is not a failed job.', 21, '#536277', 'middle')
    parts.append('</g></svg>\n')
    return '\n'.join(parts)

def build_mermaid():
    rows = ['flowchart TB']
    rows.extend(f'    {key}["{label}"]' for key, label in NODES)
    for source, target, label in EDGES:
        arrow = '-.->' if (source, target) == ('supervisor', 'owner') else '-->'
        rows.append(f'    {source} {arrow}|"{label}"| {target}')
    rows.extend([
        '    classDef main fill:#eaf2ff,stroke:#aec7eb,color:#182638',
        '    classDef supervisor fill:#fff0e3,stroke:#e4c1a3,color:#182638',
        '    classDef owner fill:#eeeafa,stroke:#c9bde8,color:#182638',
        '    classDef worker fill:#ffffff,stroke:#bfd8ce,color:#182638',
        '    classDef evidence fill:#eaf0f5,stroke:#c9d4e1,color:#182638',
        '    class main main', '    class supervisor supervisor',
        '    class owner owner', '    class build,investigate,verify worker',
        '    class evidence evidence',
    ])
    return '\n'.join(rows)+'\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--png', action='store_true', help='Also render a 2x PNG using optional Cairo/librsvg system bindings')
    args = parser.parse_args()
    (ROOT/'assets/orchestration.svg').write_text(build_svg())
    (ROOT/'diagrams/orchestration.mmd').write_text(build_mermaid())
    if args.png:
        import gi
        gi.require_version('Rsvg', '2.0')
        from gi.repository import Rsvg
        import cairo
        handle = Rsvg.Handle.new_from_file(str(ROOT/'assets/orchestration.svg'))
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH*2, HEIGHT*2)
        context = cairo.Context(surface)
        context.scale(2, 2)
        viewport = Rsvg.Rectangle()
        viewport.x, viewport.y, viewport.width, viewport.height = 0, 0, WIDTH, HEIGHT
        handle.render_document(context, viewport)
        surface.write_to_png(str(ROOT/'assets/orchestration.png'))
    print('Updated editable SVG and Mermaid graph'+(' and PNG export' if args.png else ''))

if __name__ == '__main__':
    main()
