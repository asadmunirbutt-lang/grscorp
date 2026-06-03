# Google Ads Conversion Tracking Setup Guide

## What We've Added

Your grscorp.org website now has:

1. **Google Analytics tracking** - G-542W6ZTYH8 (already installed)
2. **Google Ads conversion events** - Event-based tracking on all 20 pages
3. **Automatic event tracking** for:
   - Page scroll engagement
   - External link clicks
   - Contact form submissions (with `trackContactConversion()`)
   - Resource downloads (with `trackDownloadConversion()`)

## Step-by-Step Setup to Fix Google Ads Issues

### Step 1: Create Conversion Actions in Google Analytics

1. Go to **Google Analytics** (analytics.google.com)
2. Navigate to **Admin** > **Conversions** (left sidebar under "Data Collection and Modification")
3. Click **New Conversion Event**
4. Create the following conversion events:
   - **Event name**: `conversion` (for contact/signup)
   - **Description**: Contact form submission or conversion action
   - Click **Create**

5. Repeat for other events:
   - `file_download` - Resource downloads
   - `page_engagement` - Scroll depth tracking  
   - `click` - External link clicks

### Step 2: Link Google Analytics to Google Ads

1. In Google Analytics, go to **Admin** > **Data Streams**
2. Click your website stream
3. Scroll down to **Linked Services** > **Google Ads**
4. Click **Link Google Ads Account**
5. Select your Google Ads account and confirm

### Step 3: Create Conversion Actions in Google Ads

1. Go to **Google Ads** (ads.google.com)
2. Click **Tools & Settings** > **Conversions**
3. Click **New Conversion Action** > **Import** > **Google Analytics**
4. Select your Google Analytics property
5. Import the conversion events you created (conversion, file_download, page_engagement)
6. Assign a conversion value if desired:
   - Contact conversion: $50-100 (adjust based on your lead value)
   - Page engagement: $5 (lower value, just tracks interest)
   - External clicks: $10 (referral tracking)

### Step 4: Link Conversions to Your Campaigns

For your three campaigns flagged with issues:

**Adult Autism Signs Campaign:**
1. Go to campaign settings
2. Under "Conversion actions", select the imported conversions
3. Set appropriate conversion value tracking

**Child Autism Evaluation Campaign:**
1. Same as above
2. Enable "Conversion tracking setup" completion
3. Link to your file_download and conversion events

**IEP & S Campaign:**
1. Complete conversion action assignment
2. Ensure all conversions are properly linked

### Step 5: Verify Setup

1. **Google Analytics**: Go to **Reports** > **Conversions** to see live conversion data
2. **Google Ads**: Check campaign columns > click **Customize columns** > add "Conversions" metric
3. Within 24 hours, you should see conversion data flowing through

## Manual Conversion Tracking (Optional Enhancement)

If you have specific buttons/forms you want to track, add this to your HTML:

```html
<!-- On contact form submit button -->
<button onclick="trackContactConversion(); submitForm();">Submit</button>

<!-- On download links -->
<a href="/file.pdf" onclick="trackDownloadConversion();">Download</a>
```

## Troubleshooting

**Conversions not showing after 24 hours?**
- Verify GA tracking is working: Open website, check Google Analytics > Realtime
- Check browser console (F12) for JavaScript errors
- Ensure conversion events are created in GA AND linked to Ads

**Ad Strength still low?**
- Ensure conversion actions are assigned to all campaigns
- Wait 3-5 days for Google's AI to optimize ads
- Add more high-quality keywords and negative keywords
- Improve ad copy and landing page quality scores

**gclid not captured?**
- This happens automatically when someone clicks an Ads search ad
- Ensure gclid parameter is not being stripped by URL redirects
- Check URL parameters in Google Ads click confirmation

## Deployed Events

The following events are now automatically tracked on grscorp.org:

| Event | Trigger | Campaign Impact |
|-------|---------|-----------------|
| `conversion` | Contact form or CTA click | High (conversion action) |
| `file_download` | Resource/PDF download | Medium (engagement) |
| `page_engagement` | Scrolling > 100% viewport | Low (interest signal) |
| `click` | External link clicks | Low (traffic signal) |

## Next Steps

1. ✅ Conversion tracking code: DEPLOYED to all pages
2. ⏳ Google Analytics setup: CREATE conversion events (Steps 1-2)
3. ⏳ Google Ads setup: LINK conversions (Steps 3-4)
4. ⏳ Verification: CHECK data flow (Step 5)

Once you complete steps 2-5, all Google Ads diagnostic issues should be resolved.

---
**Estimated time to resolution**: 30-60 minutes + 24-48 hours for data to flow through systems
