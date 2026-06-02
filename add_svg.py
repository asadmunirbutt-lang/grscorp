import re
import os

svg_graphics = {
    "core-values": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='100' cy='100' r='90' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2'/><circle cx='70' cy='80' r='15' fill='#1a4d8f' opacity='0.8'/><circle cx='100' cy='60' r='15' fill='#0d7a6e' opacity='0.8'/><circle cx='130' cy='80' r='15' fill='#1a4d8f' opacity='0.8'/><circle cx='85' cy='120' r='15' fill='#0d7a6e' opacity='0.8'/><circle cx='115' cy='120' r='15' fill='#1a4d8f' opacity='0.8'/><text x='100' y='155' font-size='14' font-weight='bold' text-anchor='middle' fill='#1a2535'>Core Values</text></svg>",
    "goals": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='100' cy='100' r='50' fill='none' stroke='#e8eef7' stroke-width='8'/><circle cx='100' cy='100' r='50' fill='none' stroke='#1a4d8f' stroke-width='3' stroke-dasharray='31.4 157'/><path d='M 100 50 L 110 75 L 135 75 L 115 90 L 122 115 L 100 100 L 78 115 L 85 90 L 65 75 L 90 75 Z' fill='#0d7a6e'/><text x='100' y='165' font-size='14' font-weight='bold' text-anchor='middle' fill='#1a2535'>Our Goals</text></svg>",
    "what-causes-autism": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><ellipse cx='100' cy='100' rx='55' ry='60' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2'/><path d='M 70 70 Q 75 65 80 70 Q 85 75 80 80 Q 75 75 70 70' fill='#0d7a6e' opacity='0.8'/><path d='M 100 60 Q 105 55 110 60 Q 115 65 110 70 Q 105 65 100 60' fill='#1a4d8f' opacity='0.8'/><path d='M 130 75 Q 135 70 140 75 Q 145 80 140 85 Q 135 80 130 75' fill='#0d7a6e' opacity='0.8'/><path d='M 80 110 Q 85 105 90 110 Q 95 115 90 120 Q 85 115 80 110' fill='#1a4d8f' opacity='0.8'/><path d='M 120 115 Q 125 110 130 115 Q 135 120 130 125 Q 125 120 120 115' fill='#0d7a6e' opacity='0.8'/><text x='100' y='165' font-size='14' font-weight='bold' text-anchor='middle' fill='#1a2535'>Causes of Autism</text></svg>"
}

for page_slug, svg in svg_graphics.items():
    path = f"{page_slug}.html"
    try:
        with open(path, 'r') as f:
            html = f.read()
        html = re.sub(r'<div class="image-placeholder">Image content</div>', f'<div style="text-align: center; margin: 20px 0;">{svg}</div>', html, count=1)
        with open(path, 'w') as f:
            f.write(html)
        print(f"[OK] {page_slug}")
    except Exception as e:
        print(f"[FAIL] {page_slug}: {e}")
