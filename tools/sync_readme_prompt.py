#!/usr/bin/env python3
"""Keep the first README block identical to the plain-text global prompt."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
readme = ROOT/'README.md'
text = readme.read_text()
assert text.startswith('```text\n')
end = text.index('\n```\n', len('```text\n')) + len('\n```\n')
prompt = (ROOT/'prompts/global-orchestration.txt').read_text().rstrip()
readme.write_text('```text\n'+prompt+'\n```\n'+text[end:])
print('README first prompt block synchronized')
