import re

svg_dict = {
    "core-values": '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; margin: 30px 0;"><rect x="50" y="20" width="120" height="120" fill="#ff6b6b" rx="10"/><text x="110" y="85" font-size="40" text-anchor="middle" fill="white" font-weight="bold">✓</text><text x="110" y="145" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Empowerment</text><rect x="240" y="20" width="120" height="120" fill="#4ecdc4" rx="10"/><text x="300" y="85" font-size="40" text-anchor="middle" fill="white" font-weight="bold">❤</text><text x="300" y="145" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Compassion</text><rect x="430" y="20" width="120" height="120" fill="#ffd93d" rx="10"/><text x="490" y="85" font-size="40" text-anchor="middle" fill="white" font-weight="bold">🤝</text><text x="490" y="145" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Inclusion</text><rect x="50" y="200" width="120" height="120" fill="#95e1d3" rx="10"/><text x="110" y="265" font-size="40" text-anchor="middle" fill="white" font-weight="bold">💡</text><text x="110" y="325" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Innovation</text><rect x="240" y="200" width="120" height="120" fill="#a8d8ea" rx="10"/><text x="300" y="265" font-size="40" text-anchor="middle" fill="white" font-weight="bold">🎯</text><text x="300" y="325" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Excellence</text><rect x="430" y="200" width="120" height="120" fill="#c7a8ea" rx="10"/><text x="490" y="265" font-size="40" text-anchor="middle" fill="white" font-weight="bold">🌟</text><text x="490" y="325" font-size="14" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Respect</text></svg>',
    "background": '<svg viewBox="0 0 600 350" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; margin: 30px 0;"><text x="300" y="40" font-size="18" font-weight="bold" fill="#1a4d8f" text-anchor="middle">Organization Timeline</text><circle cx="100" cy="150" r="35" fill="#ff6b6b"/><text x="100" y="160" font-size="12" fill="white" font-weight="bold" text-anchor="middle">Founded</text><text x="100" y="220" font-size="13" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Established</text><line x1="135" y1="150" x2="265" y2="150" stroke="#0d7a6e" stroke-width="3"/><circle cx="300" cy="150" r="35" fill="#4ecdc4"/><text x="300" y="160" font-size="12" fill="white" font-weight="bold" text-anchor="middle">Growth</text><text x="300" y="220" font-size="13" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Expanding</text><line x1="335" y1="150" x2="465" y2="150" stroke="#0d7a6e" stroke-width="3"/><circle cx="500" cy="150" r="35" fill="#ffd93d"/><text x="500" y="160" font-size="12" fill="white" font-weight="bold" text-anchor="middle">Today</text><text x="500" y="220" font-size="13" fill="#1a4d8f" font-weight="bold" text-anchor="middle">Thriving</text><text x="300" y="290" font-size="14" fill="#1a4d8f" text-anchor="middle" font-weight="bold">Serving Autism Community Worldwide</text></svg>',
}

count = 0
for page_slug, svg in svg_dict.items():
    try:
        with open(f"{page_slug}.html", 'r', encoding='utf-8') as f:
            html = f.read()

        # Remove old SVG
        html = re.sub(r'<div style="text-align: center; margin: 40px 0;"><svg.*?</svg></div>', '', html, flags=re.DOTALL)

        # Insert new SVG
        svg_html = f'<div style="text-align: center; margin: 40px 0;">{svg}</div>'
        html = html.replace('<hr style="margin: 40px 0; border: none; border-top: 1px solid var(--border);">', f'{svg_html}\n    <hr style="margin: 40px 0; border: none; border-top: 1px solid var(--border);">')

        with open(f"{page_slug}.html", 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        print(f"[OK] {page_slug}")
    except Exception as e:
        print(f"[FAIL] {page_slug}: {str(e)}")

print(f"\nUpdated {count} pages")
