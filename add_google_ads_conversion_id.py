import os
import re

# Google Ads Conversion ID from the diagnostic panel
CONVERSION_ID = "AW-1133270985"

# Google Ads conversion tracking tag - goes in <head>
GOOGLE_ADS_TAG = '''    <!-- Google Ads Conversion Tracking Tag -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{}');
    </script>'''.format(CONVERSION_ID, CONVERSION_ID)

def add_google_ads_tag(html_content):
    """Add Google Ads conversion tracking tag after GA tag"""
    
    # Check if already has this conversion ID
    if CONVERSION_ID in html_content:
        return None
    
    # Find the Google Analytics script end and add our tag after it
    # Look for the GA config closing script tag
    ga_pattern = r"(gtag\('config', 'G-542W6ZTYH8'\);.*?</script>)"
    
    if re.search(ga_pattern, html_content, re.DOTALL):
        html_content = re.sub(
            ga_pattern,
            r'\1\n' + GOOGLE_ADS_TAG,
            html_content,
            flags=re.DOTALL
        )
        return html_content
    
    return None

updated = 0
for filename in os.listdir('.'):
    if not filename.endswith('.html'):
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = add_google_ads_tag(content)
        
        if new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("[OK] {} - Google Ads tag {} added".format(filename, CONVERSION_ID))
            updated += 1
        elif CONVERSION_ID in content:
            print("[SKIP] {} - Already has Google Ads tag".format(filename))
        else:
            print("[SKIP] {} - GA tag not found".format(filename))
    
    except Exception as e:
        print("[ERR] {} - {}".format(filename, str(e)))

print("\nTotal updated: {}".format(updated))
print("Conversion ID: {}".format(CONVERSION_ID))

