import os
import re

grscorp_dir = os.getcwd()

GOOGLE_ADS_HEAD_CODE = '''    <!-- Google Ads Conversion Tracking -->
    <script>
      (function() {
        const urlParams = new URLSearchParams(window.location.search);
        const gclid = urlParams.get('gclid');
        if (gclid && window.gtag) {
          gtag('config', 'G-542W6ZTYH8', {
            'allow_google_signals': true,
            'allow_ad_personalization_signals': true
          });
        }
      })();
    </script>'''

CONVERSION_EVENT_CODE = '''    <!-- Google Ads Conversion Events -->
    <script>
      function trackContactConversion() {
        if (typeof gtag !== 'undefined') {
          gtag('event', 'conversion', {
            'value': 1.0,
            'currency': 'USD',
            'transaction_id': 'contact_' + Date.now()
          });
        }
      }

      function trackDownloadConversion() {
        if (typeof gtag !== 'undefined') {
          gtag('event', 'file_download', {
            'file_name': 'resource'
          });
        }
      }

      let scrollTracked = false;
      window.addEventListener('scroll', function() {
        if (!scrollTracked && (window.scrollY > window.innerHeight)) {
          if (typeof gtag !== 'undefined') {
            gtag('event', 'page_engagement', {
              'engagement_type': 'scroll',
              'scroll_depth': Math.round((window.scrollY / document.documentElement.scrollHeight) * 100)
            });
          }
          scrollTracked = true;
        }
      });

      document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (link && link.href && (link.href.startsWith('http') || link.href.startsWith('//'))) {
          if (!link.href.includes('grscorp.org')) {
            if (typeof gtag !== 'undefined') {
              gtag('event', 'click', {
                'link_url': link.href,
                'link_text': link.textContent
              });
            }
          }
        }
      });
    </script>'''

def add_conversion_tracking(html_content):
    if 'trackContactConversion' in html_content:
        return None
    
    if "gtag('config', 'G-542W6ZTYH8')" not in html_content:
        return None
    
    # Add Google Ads head code after GA config
    html_content = html_content.replace(
        "gtag('config', 'G-542W6ZTYH8');",
        "gtag('config', 'G-542W6ZTYH8');" + GOOGLE_ADS_HEAD_CODE
    )
    
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', CONVERSION_EVENT_CODE + '\n</body>')
    
    return html_content

updated = 0
for filename in os.listdir(grscorp_dir):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(grscorp_dir, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = add_conversion_tracking(content)
        
        if new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("[OK] {} - Conversion tracking added".format(filename))
            updated += 1
        elif 'trackContactConversion' in content:
            print("[SKIP] {} - Already has tracking".format(filename))
        else:
            print("[SKIP] {} - No GA tag found".format(filename))
    
    except Exception as e:
        print("[ERR] {} - {}".format(filename, str(e)))

print("\nTotal updated: {}".format(updated))

