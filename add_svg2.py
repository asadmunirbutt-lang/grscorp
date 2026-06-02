import re
import os

svg_graphics = {
    "core-values": "<svg><circle cx='100' cy='100' r='90' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2'/><text x='100' y='155'>Core Values</text></svg>",
    "background": "<svg><rect x='30' y='40' width='140' height='100' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2' rx='5'/><text x='100' y='165'>Organization</text></svg>",
    "board-members": "<svg><circle cx='50' cy='60' r='18' fill='#1a4d8f' opacity='0.8'/><circle cx='100' cy='50' r='18' fill='#0d7a6e' opacity='0.8'/><circle cx='150' cy='60' r='18' fill='#1a4d8f' opacity='0.8'/><text x='100' y='165'>Our Team</text></svg>",
    "goals": "<svg><circle cx='100' cy='100' r='50' fill='none' stroke='#1a4d8f' stroke-width='3'/><path d='M 100 50 L 110 75 L 135 75 L 115 90 L 122 115 L 100 100 L 78 115 L 85 90 L 65 75 L 90 75 Z' fill='#0d7a6e'/><text x='100' y='165'>Our Goals</text></svg>",
    "purpose": "<svg><circle cx='100' cy='80' r='35' fill='#1a4d8f' opacity='0.8'/><path d='M 100 50 L 115 70 L 130 75 Q 100 95 70 75 L 85 70 Z' fill='#ffd700'/><text x='100' y='165'>Our Purpose</text></svg>",
}

for page_slug, svg in svg_graphics.items():
    path = f"{page_slug}.html"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = re.sub(r'<div class="image-placeholder">Image content</div>', f'<div style="text-align: center; margin: 20px 0;">{svg}</div>', html, count=1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[OK] {page_slug}")
    except Exception as e:
        print(f"[FAIL] {page_slug}: {str(e)[:40]}")

print("SVG graphics added!")
