# Google Ads Conversion Actions Setup - Complete Instructions

## Your Account Details
- **Google Ads Account ID**: 1436034674
- **Google Ads Conversion ID**: AW-11332709859
- **Website**: grscorp.us
- **Campaigns to Configure**:
  1. Adult Autism Signs
  2. Child Autism Evaluation  
  3. IEP & S

## What's Already Done
âœ… Google Analytics installed (G-542W6ZTYH8)
âœ… Google Ads conversion tag installed (AW-11332709859)
âœ… Event tracking code deployed (conversion, file_download, page_engagement events)

## What You Need to Do: Create Conversion Actions

### Method 1: Via Google Ads UI (Recommended - Takes 10 minutes)

**Step 1: Access Conversions**
1. Go to https://ads.google.com
2. Click **Tools & Settings** (wrench icon, top right)
3. Under "Measurement" section, click **Conversions**

**Step 2: Create First Conversion Action - "Contact Submission"**
1. Click **+ New Conversion Action**
2. Select **Website** (blue button)
3. Enter tracking details:
   - **Conversion name**: `Contact Form Submission`
   - **Conversion category**: Leads
   - **Conversion value**: $75 (adjust based on your lead value)
   - **Count**: Every conversion
   - **Attribution model**: Data-driven (if available) or Last Click

4. Under "Conversion tracking source", select:
   - **Platform**: Google Analytics 4
   - **Property**: Select your GA4 property
   - **Event name**: `conversion`

5. Click **Create and Continue**

**Step 3: Create Second Conversion Action - "Resource Download"**
1. Click **+ New Conversion Action**
2. Select **Website**
3. Enter tracking details:
   - **Conversion name**: `Resource Download`
   - **Conversion category**: Leads
   - **Conversion value**: $25
   - **Count**: Every conversion

4. Under "Conversion tracking source":
   - **Platform**: Google Analytics 4
   - **Event name**: `file_download`

5. Click **Create and Continue**

**Step 4: Create Third Conversion Action - "Page Engagement"** (Optional but recommended)
1. Click **+ New Conversion Action**
2. Select **Website**
3. Enter tracking details:
   - **Conversion name**: `High Engagement (Page Scroll)`
   - **Conversion category**: Engagement
   - **Conversion value**: $5
   - **Count**: Only count once per day

4. Under "Conversion tracking source":
   - **Platform**: Google Analytics 4
   - **Event name**: `page_engagement`

5. Click **Create and Continue**

---

### Step 5: Link Conversions to Your Campaigns

**For EACH of your 3 campaigns:**

1. Go to **Campaigns** (left sidebar)
2. Click on campaign name (e.g., "Adult Autism Signs")
3. Click **Settings** tab
4. Scroll to **Conversion actions**
5. Click the pencil icon to edit
6. **Check the boxes** for:
   - âœ“ Contact Form Submission
   - âœ“ Resource Download
   - âœ“ High Engagement (Page Scroll) [optional]

7. Click **Save**

**Repeat for:**
- Child Autism Evaluation campaign
- IEP & S campaign

---

## Method 2: Via Google Analytics (If Google Ads link fails)

If Google Ads conversion import doesn't work:

1. Go to **Google Analytics** (analytics.google.com)
2. **Admin** â†’ **Events**
3. Look for events: `conversion`, `file_download`, `page_engagement`
4. Mark them as **Conversion Events** (toggle switch)
5. Wait 24 hours for data to sync to Google Ads

---

## Verification Steps

**After 1-2 hours:**
1. Go to Google Ads â†’ **Campaigns**
2. Add column: **Conversions** (customize columns)
3. Should show conversion tracking is active

**After 24-48 hours:**
1. Should see actual conversion data flowing
2. Campaign diagnostics errors should clear
3. "Ad Strength" rating should improve

---

## Troubleshooting

### "Can't find event in Google Analytics"
- Go to GA4 â†’ Real-time
- Trigger the event on your website (scroll page, click external link, etc.)
- Verify event appears in Real-time view
- Wait 24 hours, then try creating conversion again

### "Conversions not showing in Ads"
1. Verify GA and Ads are linked:
   - GA â†’ Admin â†’ Data Streams â†’ Linked Services
   - Should show Google Ads connected

2. Check conversion actions exist:
   - Ads â†’ Tools â†’ Conversions
   - All 3 should be listed

3. Check campaign assignment:
   - Ads â†’ Campaigns â†’ Settings
   - All 3 conversions should be checked

### "Campaign still says misconfigured"
1. Refresh Google Ads page (Ctrl+F5)
2. Wait 30 minutes (Google's system update lag)
3. Clear browser cache
4. Try in incognito mode

---

## Event Details for Reference

These events are firing automatically on your website:

| Event Name | Trigger | Importance |
|-----------|---------|-----------|
| `conversion` | Any click or form submission | **CRITICAL** - Main conversion |
| `file_download` | Resource/PDF download | **HIGH** - Engagement signal |
| `page_engagement` | User scrolls page | **MEDIUM** - Interest indicator |
| `click` | External link click | LOW - Referral tracking |

---

## Expected Timeline

| Task | Timeline | Status |
|------|----------|--------|
| Install Google Ads tag | âœ… Complete | Deployed |
| Create conversion actions | 10 minutes | **â† You are here** |
| Link conversions to campaigns | 5 minutes | Pending |
| Google Ads detection | 5-10 min after linking | Pending |
| Data flow to Ads | 24-48 hours | Pending |
| Campaign diagnostics clear | After data flows | Pending |

---

## Still Having Issues?

If conversions don't appear after 48 hours:
1. Check if events are firing: GA4 â†’ Real-time
2. Verify gclid parameter is captured (comes from Ads clicks)
3. Check for JavaScript errors: Press F12 â†’ Console tab
4. Ensure conversion value is > $0



