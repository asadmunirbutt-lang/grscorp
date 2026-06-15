import re
import os

pages = [
    "core-values",
    "background",
    "board-members",
    "goals",
    "purpose",
    "what-causes-autism",
    "first-concern-to-action",
    "learn-the-sign-of-autism",
    "sensory-issues",
    "autism-diagnosis-criteria",
    "medical-conditions-associated-with-autism",
    "gallery",
    "training-services"
]

output_dir = "."

# CSS for image placeholders
placeholder_css = '''
        .image-placeholder {
            background: linear-gradient(135deg, #f0f4f8 0%, #e8eef7 100%);
            border: 2px dashed var(--border);
            border-radius: 8px;
            padding: 40px 20px;
            text-align: center;
            color: var(--text-soft);
            font-size: 14px;
            margin: 20px 0;
            min-height: 200px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .image-placeholder::before {
            content: "📸";
            font-size: 48px;
            margin-bottom: 12px;
            opacity: 0.5;
        }
'''

print("Cleaning up broken images from all 13 pages...\n")

for page_slug in pages:
    filepath = os.path.join(output_dir, f"{page_slug}.html")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        original_size = len(html)

        # Remove all img tags that point to external URLs
        html = re.sub(
            r'<img[^>]*data-src="https://grscorp\.us[^"]*"[^>]*>',
            '<div class="image-placeholder">Image content</div>',
            html,
            flags=re.IGNORECASE
        )

        # Remove remaining img tags with broken src attributes
        html = re.sub(
            r'<img[^>]*src="data:image/svg[^"]*"[^>]*>',
            '<div class="image-placeholder">Image content</div>',
            html,
            flags=re.IGNORECASE
        )

        # Add placeholder CSS if not already present
        if 'image-placeholder' in html and '.image-placeholder' not in html:
            # Find the closing </style> tag and insert our CSS before it
            html = html.replace(
                '        @media (max-width: 768px) {',
                placeholder_css + '\n        @media (max-width: 768px) {'
            )

        # Clean up excessive whitespace (multiple blank lines)
        html = re.sub(r'\n\n\n+', '\n\n', html)

        new_size = len(html)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

        img_count = html.count('class="image-placeholder"')
        size_diff = original_size - new_size
        print(f"[OK] {page_slug:<40} - {img_count} placeholders | -{size_diff} bytes")

    except Exception as e:
        print(f"[FAIL] {page_slug}: {str(e)[:50]}")

print("\n" + "="*60)
print("✓ Cleanup complete! All broken images replaced with placeholders.")
print("  Pages are now clean and ready for deployment.")
