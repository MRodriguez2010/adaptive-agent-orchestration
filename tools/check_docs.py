#!/usr/bin/env python3
"""Check prompt synchronization, local documentation links and graph exports."""
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET
import runpy

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT/'README.md').read_text()
assert readme.startswith('```text\n'), 'The copyable prompt must be the very first README block'
first = readme[len('```text\n'):readme.index('\n```\n')]
assert first == (ROOT/'prompts/global-orchestration.txt').read_text().rstrip(), 'Prompt drift'
checked = 0
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        target = match.group(1).strip().split('#', 1)[0]
        if not target or re.match(r'^[a-z]+:', target):
            continue
        assert (path.parent/target).resolve().is_file(), f'Broken local link: {path.name} -> {target}'
        checked += 1
builder = runpy.run_path(str(ROOT/'tools/build_diagram.py'))
assert '\n# '+builder['PROJECT_TITLE']+'\n' in readme, 'README/project title drift'
assert (ROOT/'assets/orchestration.svg').read_text() == builder['build_svg'](), 'SVG/layout drift'
assert (ROOT/'diagrams/orchestration.mmd').read_text() == builder['build_mermaid'](), 'Mermaid/layout drift'
svg = ET.parse(ROOT/'assets/orchestration.svg').getroot()
actual = {n.attrib['data-node'] for n in svg.iter() if 'data-node' in n.attrib}
assert actual == {key for key, _ in builder['NODES']}
assert not any(n.tag.split('}')[-1] in {'script','foreignObject'} for n in svg.iter())
raw = (ROOT/'assets/orchestration.png').read_bytes()
assert raw[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', raw[16:24]) == (3200,2760)
print(f'PASS: first prompt synchronized; {checked} local links; 7 graph nodes; SVG/Mermaid sources exact; PNG 3200x2760')
