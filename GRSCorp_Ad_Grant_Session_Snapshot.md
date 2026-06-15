# GRSCorp Google Ad Grant Campaign Setup - Session Snapshot
**Date:** June 1, 2026  
**Project:** Autism-focused Google Ad Grant optimization for GRSCorp  
**Status:** Campaign 2 created (1 ad disapproved - needs investigation)

---

## Project Overview
- **Organization:** Global Relief and Support Corporation (GRSCorp)
- **Main Site:** grscorp.us  
- **Blog Site:** blogs.grscorp.us  
- **GA4 Property:** GRSCORP-GA4 (ID: 406316683)
- **Google Ad Grant Budget:** $329/day (~$10K/month)
- **Budget Allocation:** $82-90 per campaign (4 total campaigns)

---

## Completed Work

### 1. GA4 & Conversion Tracking Setup ✅
- **GA4 Status:** Linked to Google Ads account
- **GA4 Property Connected:** 404639534 (grscorp.us) + New data stream for blogs.grscorp.us
- **Conversion Action:** "Engagement" (Local actions - Other engagements)
  - Status: Active
  - Source: Google hosted
  - Measurement ID: G-542W6ZTYH8
- **Data Streams Added:** 
  - grscorp.us (existing)
  - blogs.grscorp.us (newly created to track blog subdomain)

### 2. Google Analytics Tag Installation ✅
- **Tag Added To:**
  - index.html (blog home)
  - BLOG_POST_TEMPLATE.html (template)
  - All three blog post pages
- **Measurement ID:** G-542W6ZTYH8
- **GitHub Repo:** https://github.com/asadmunirbutt-lang/grscorp-blogs
- **Status:** Committed and pushed to master

### 3. Blog Posts Created & Deployed ✅
**All posts include:**
- Google Analytics tag (gtag.js with ID G-542W6ZTYH8)
- Colorful, professional design with gradients
- Statistics and data visualizations
- Color-coded themes

**Blog Posts:**
1. **how-to-get-autism-evaluation.html** (Campaign 2 landing page)
   - URL: blogs.grscorp.us/posts/how-to-get-autism-evaluation.html
   - Theme: Purple/Blue gradient
   - Stats: "1 in 36 children", "4-8 weeks evaluation", "3-5 hours assessment"

2. **autism-iep-guide.html** (Campaign 3 landing page)
   - URL: blogs.grscorp.us/posts/autism-iep-guide.html
   - Theme: Red/Orange gradient
   - Stats: "14% of school-age children receive IEP services"

3. **signs-of-autism-in-adults.html** (Campaign 4 landing page)
   - URL: blogs.grscorp.us/posts/signs-of-autism-in-adults.html
   - Theme: Green/Teal gradient
   - Stats: "25%+ autism diagnoses in adults"

---

## Campaigns Status

### Campaign 1: Autism Screening Tool ✅ CREATED
- **Landing Page:** blogs.grscorp.us/autism-screening-test.html
- **Campaign Type:** Search
- **Objective:** Leads
- **Status:** Paused initially, ready to enable
- **Conversion Action:** Engagement
- **Bidding:** Maximize Conversions
- **Daily Budget:** TBD (~$82-90)

### Campaign 2: Child Autism Evaluation ⚠️ IN PROGRESS
- **Landing Page:** blogs.grscorp.us/posts/how-to-get-autism-evaluation.html
- **Campaign Type:** Search
- **Objective:** Leads
- **Status:** Created, but **1 ad disapproved** (needs investigation)
- **Conversion Action:** Engagement
- **Bidding:** Maximize Conversions
- **Daily Budget:** To be set (~$82-90)
- **Keywords Added:** autism evaluation, child autism assessment, autism diagnosis, how to get autism evaluated, autism testing for children, evaluate autism in children, professional autism evaluation
- **AI Max:** Enabled

**Known Issues:**
- Initial landing page check returned 404 (due to GitHub Pages deployment delay)
- "Continue with known issue" was selected to proceed
- Ad disapproval reason: needs to be checked

### Campaign 3: IEP & School Rights ⏳ NOT YET CREATED
- **Landing Page:** blogs.grscorp.us/posts/autism-iep-guide.html
- **Daily Budget:** ~$82-90
- **Expected Keywords:** IEP autism, autism school rights, autism education advocacy, etc.

### Campaign 4: Adult Autism Signs ⏳ NOT YET CREATED
- **Landing Page:** blogs.grscorp.us/posts/signs-of-autism-in-adults.html
- **Daily Budget:** ~$82-90
- **Expected Keywords:** adult autism signs, autism in adults, undiagnosed autism, etc.

---

## Outstanding Tasks

### Immediate (Next Session)
1. ✋ **Check Campaign 2 Ad Disapproval**
   - Click "1 ad disapproved" notification
   - Understand why ad was disapproved
   - Fix the issue or request exception
   - Confirm campaign can run

2. ⏳ **Set Campaign 2 Daily Budget**
   - Budget: $82/day (within $80-90 range)
   - Confirm Maximize Conversions bidding

3. ✅ **Verify Blog Pages Are Live**
   - Check that blogs.grscorp.us pages are returning 200 OK (not 404)
   - Google will re-check automatically once deployed

### Secondary (Once Campaign 2 is Live)
4. Create Campaign 3: Child Autism Evaluation
   - Landing: blogs.grscorp.us/posts/autism-iep-guide.html
   - Budget: ~$82/day
   - Same settings as Campaign 2

5. Create Campaign 4: Adult Autism Signs
   - Landing: blogs.grscorp.us/posts/signs-of-autism-in-adults.html
   - Budget: ~$82/day
   - Same settings as Campaign 2

### Final Steps
6. Re-enable Campaign 1 (Autism Screening Tool)
   - Set daily budget: ~$82/day
   - Confirm it's ready to run

7. Monitor Conversions
   - Watch for Engagement events in GA4
   - Monitor campaign performance
   - Optimize based on data

---

## Key Settings (All Campaigns)

**Consistent across all 4 campaigns:**
- Campaign Type: Search only
- Objective: Leads
- Targeting: United States
- Language: English
- Bidding Strategy: Maximize Conversions
- Conversion Action: Engagement (GA4)
- Daily Budget: $82-90/day each
- AI Max: Enabled
- Text Customization: Enabled
- Final URL Expansion: Enabled

---

## Important URLs & IDs

**Google Ads Account:**
- Status: Active
- Ad Grant: $329/day available
- Optimization Score: 0% → improving as campaigns are set up

**GA4:**
- Account Email: asadmunirbutt-lang@gmail.com
- Property: GRSCORP-GA4
- Measurement ID: G-542W6ZTYH8

**GitHub Repository:**
- https://github.com/asadmunirbutt-lang/grscorp-blogs
- Branch: master
- Last commits: Blog post creation & styling updates

**Blog Domain:**
- https://blogs.grscorp.us/ (GitHub Pages deployment)
- Deployment Status: ~1-2 minutes after push (may still be deploying)

---

## Notes for Next Session

1. **GitHub Pages Deployment**: Blog posts were just pushed and may take 1-2 minutes to fully deploy. If you see 404 errors, wait and retry.

2. **Ad Disapprovals**: Campaign 2 has 1 ad disapproved. Check the notification to see the reason (likely policy-related or destination issue).

3. **Conversion Tracking**: GA4 Engagement action is already configured and active. Pages have the gtag installed. No additional setup needed for conversion measurement.

4. **Budget Breakdown**: $329/day ÷ 4 campaigns = $82.25/day per campaign. Each should be set to $82 or $85/day.

5. **Campaign 1 Status**: Already created but may be paused. Will need to set budget and enable once Campaigns 2-4 are confirmed working.

---

**End of Snapshot**
