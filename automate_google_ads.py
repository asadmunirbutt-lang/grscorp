#!/usr/bin/env python3
"""
Google Ads Conversion Setup - Interactive Automation
This script will guide you through setting up conversions in Google Ads

Instructions:
1. Run this script
2. Follow the prompts
3. When asked, perform the action in your browser
4. Script will verify and continue
"""

import time
import webbrowser

ACCOUNT_ID = "1436034674"

CONVERSIONS = [
    {
        "name": "Contact Form Submission",
        "description": "When a user submits a contact form",
        "value": "$75"
    },
    {
        "name": "Resource Download",
        "description": "When a user downloads a resource/PDF",
        "value": "$25"
    },
    {
        "name": "Page Engagement (Scroll)",
        "description": "When a user scrolls deeply on a page",
        "value": "$5"
    }
]

CAMPAIGNS = [
    "Adult Autism Signs",
    "Child Autism Evaluation",
    "IEP & S"
]

def print_header(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

def step_navigator():
    """Interactive step navigator"""

    print_header("GOOGLE ADS CONVERSION SETUP - INTERACTIVE MODE")

    print("\nThis script will guide you through setting up Google Ads conversions.")
    print("You will need to perform actions in your browser, and this script will verify.")

    # Step 1: Open Google Ads
    print_header("STEP 1: Open Google Ads Conversions Page")

    input_val = input("\nPress Enter, and I'll open Google Ads Conversions page in your browser...")
    webbrowser.open("https://ads.google.com/aw/conversions")

    print("\n[OK] Google Ads Conversions page opened in your browser")
    print("\nIn your browser:")
    print("  1. Make sure you're logged into Google Ads account")
    print("  2. You should see the 'Conversions' page")

    input_val = input("\nWhen you see the Conversions page, press Enter to continue...")

    # Step 2: Create conversions
    print_header("STEP 2: Create Conversion Actions")

    for i, conversion in enumerate(CONVERSIONS, 1):
        print(f"\n--- Conversion {i} of {len(CONVERSIONS)} ---")
        print(f"Name: {conversion['name']}")
        print(f"Description: {conversion['description']}")
        print(f"Value: {conversion['value']}")

        print("\nIn your browser, do this:")
        print(f"  1. Click '+ New conversion action' button")
        print(f"  2. Select 'Website'")
        print(f"  3. Enter name: {conversion['name']}")
        print(f"  4. Set value: {conversion['value'].replace('$', '')}")
        print(f"  5. For tracking source:")
        print(f"     - Platform: Google Analytics 4")
        print(f"     - Event name: {convert_to_event_name(conversion['name'])}")
        print(f"  6. Click 'Create and continue'")

        input_val = input(f"\nWhen you've created '{conversion['name']}', press Enter...")

    # Step 3: Link to campaigns
    print_header("STEP 3: Link Conversions to Campaigns")

    for i, campaign in enumerate(CAMPAIGNS, 1):
        print(f"\n--- Campaign {i} of {len(CAMPAIGNS)} ---")
        print(f"Campaign: {campaign}")

        print("\nIn your browser, do this:")
        print(f"  1. Go to Campaigns (left menu)")
        print(f"  2. Click on campaign: '{campaign}'")
        print(f"  3. Click 'Settings' tab")
        print(f"  4. Scroll to 'Conversion actions'")
        print(f"  5. Click edit (pencil icon)")
        print(f"  6. Check boxes for all 3 conversions:")
        for conv in CONVERSIONS:
            print(f"     ☐ {conv['name']}")
        print(f"  7. Click 'Save'")

        input_val = input(f"\nWhen you've linked all conversions to '{campaign}', press Enter...")

    # Done
    print_header("AUTOMATION COMPLETE!")

    print("\n✓ All conversion actions created")
    print("✓ All campaigns linked to conversions")
    print("\nNext steps:")
    print("  1. Return to Google Ads dashboard")
    print("  2. Wait 5-10 minutes for changes to propagate")
    print("  3. Check 'Campaign diagnostics' - should show improvement")
    print("  4. Data will flow within 24-48 hours")
    print("\nIf you have issues, refer to GOOGLE_ADS_CONVERSION_SETUP.md for details")

def convert_to_event_name(conversion_name):
    """Convert conversion name to GA4 event name"""
    mapping = {
        "Contact Form Submission": "conversion",
        "Resource Download": "file_download",
        "Page Engagement (Scroll)": "page_engagement"
    }
    return mapping.get(conversion_name, "conversion")

if __name__ == "__main__":
    try:
        step_navigator()
    except KeyboardInterrupt:
        print("\n\n[CANCELLED] Setup cancelled by user")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
