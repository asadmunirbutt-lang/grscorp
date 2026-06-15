import os
import re

# Proper Google Ads tag setup
GOOGLE_TAGS = '''    <!-- Google Analytics (GA4) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-542W6ZTYH8"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-542W6ZTYH8');
    </script>

    <!-- Google Ads Conversion Tracking -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=AW-1133270985"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'AW-1133270985');
    </script>'''

def fix_google_tags(html_content):
    """Remove old/malformed tags and insert clean ones"""
    
    # Remove all old gtag scripts and Google tag comments
    html_content = re.sub(
        r'<!--.*?Google.*?tag.*?-->.*?</script>',
        '',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Remove duplicate gtag script blocks
    html_content = re.sub(
        r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=.*?</script>\s*',
        '',
        html_content,
        flags=re.DOTALL
    )
    
    # Remove any leftover Google Ads conversion tracking comments/scripts
    html_content = re.sub(
        r'<!--.*?Google Ads.*?-->.*?</script>\s*',
        '',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Find the closing </head> tag
    if '</head>' in html_content:
        # Insert our clean tags before </head>
        html_content = html_content.replace(
            '</head>',
            GOOGLE_TAGS + '\n  </head>'
        )
    
    return html_content

# Process all HTML files
os.chdir('/c/Users/Asadm/AppData/Local/Temp/grscorp')

updated = 0
for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the tags
        new_content = fix_google_tags(content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"[OK] Fixed tags in {filename}")
        updated += 1
    
    except Exception as e:
        print(f"[ERROR] {filename}: {e}")

print(f"\nFixed {updated} files")

