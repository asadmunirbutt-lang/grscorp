import re

svg_graphics = {
    "what-causes-autism": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><ellipse cx='100' cy='100' rx='55' ry='60' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2'/><path d='M 70 70 Q 75 65 80 70 Q 85 75 80 80' fill='#0d7a6e' opacity='0.8'/><text x='100' y='165' font-size='14' font-weight='bold'>Causes of Autism</text></svg>",
    "first-concern-to-action": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='30' cy='100' r='18' fill='#1a4d8f' opacity='0.8'/><text x='30' y='105' fill='white' text-anchor='middle'>1</text><line x1='48' y1='100' x2='82' y2='100' stroke='#0d7a6e' stroke-width='2'/><circle cx='100' cy='100' r='18' fill='#0d7a6e'/><text x='100' y='105' fill='white' text-anchor='middle'>2</text><line x1='118' y1='100' x2='152' y2='100' stroke='#1a4d8f' stroke-width='2'/><circle cx='170' cy='100' r='18' fill='#1a4d8f'/><text x='170' y='105' fill='white' text-anchor='middle'>3</text><text x='100' y='165'>Action Steps</text></svg>",
    "learn-the-sign-of-autism": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='100' cy='80' r='28' fill='#1a4d8f' opacity='0.8'/><circle cx='90' cy='75' r='4' fill='white'/><circle cx='110' cy='75' r='4' fill='white'/><path d='M 100 85 Q 100 90 95 95' stroke='white' stroke-width='2' fill='none'/><text x='100' y='165'>Autism Signs</text></svg>",
    "sensory-issues": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='100' cy='100' r='65' fill='none' stroke='#e8eef7' stroke-width='3'/><circle cx='100' cy='100' r='50' fill='none' stroke='#1a4d8f' stroke-width='2' opacity='0.6'/><circle cx='100' cy='50' r='6' fill='#1a4d8f'/><circle cx='150' cy='100' r='6' fill='#0d7a6e'/><circle cx='100' cy='150' r='6' fill='#1a4d8f'/><circle cx='50' cy='100' r='6' fill='#0d7a6e'/><text x='100' y='30' font-size='11' fill='#6b7c8d'>Sound</text><text x='100' y='165'>Sensory</text></svg>",
    "autism-diagnosis-criteria": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><rect x='40' y='50' width='120' height='100' fill='none' stroke='#1a4d8f' stroke-width='2' rx='5'/><line x1='40' y1='75' x2='160' y2='75' stroke='#1a4d8f'/><line x1='40' y1='100' x2='160' y2='100' stroke='#1a4d8f'/><line x1='40' y1='125' x2='160' y2='125' stroke='#1a4d8f'/><text x='100' y='165'>Diagnostic Criteria</text></svg>",
    "medical-conditions-associated-with-autism": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><circle cx='100' cy='100' r='45' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2'/><line x1='100' y1='55' x2='100' y2='40' stroke='#1a4d8f' stroke-width='2'/><line x1='145' y1='100' x2='160' y2='100' stroke='#1a4d8f' stroke-width='2'/><line x1='100' y1='145' x2='100' y2='160' stroke='#1a4d8f' stroke-width='2'/><line x1='55' y1='100' x2='40' y2='100' stroke='#1a4d8f' stroke-width='2'/><text x='100' y='165'>Medical Info</text></svg>",
    "gallery": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><rect x='40' y='50' width='120' height='100' fill='#e8eef7' stroke='#1a4d8f' stroke-width='2' rx='5'/><rect x='50' y='60' width='30' height='30' fill='#1a4d8f' opacity='0.6'/><circle cx='80' cy='75' r='8' fill='#0d7a6e'/><rect x='90' y='60' width='30' height='30' fill='#0d7a6e'/><polygon points='105,90 115,80 125,90' fill='#1a4d8f'/><text x='100' y='165'>Gallery</text></svg>",
    "training-services": "<svg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg' style='max-width: 100%; height: auto;'><rect x='45' y='50' width='110' height='90' fill='none' stroke='#1a4d8f' stroke-width='2'/><rect x='50' y='55' width='100' height='15' fill='#1a4d8f' opacity='0.8'/><text x='100' y='66' font-size='10' fill='white' text-anchor='middle'>Training</text><circle cx='65' cy='85' r='6' fill='#0d7a6e'/><circle cx='100' cy='85' r='6' fill='#1a4d8f'/><circle cx='135' cy='85' r='6' fill='#0d7a6e'/><text x='100' y='165'>Services</text></svg>"
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

print("All remaining SVG graphics added!")
