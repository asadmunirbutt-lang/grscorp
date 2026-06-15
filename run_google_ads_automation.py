#!/usr/bin/env python3
"""
Google Ads Conversion Setup - Full Automation
Uses Selenium to automate conversion creation and campaign linking
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import subprocess
import sys
import os

class GoogleAdsAutomation:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.actions = None

    def start_chrome_with_debugging(self):
        """Start Chrome with remote debugging enabled"""
        print("[*] Starting Chrome with remote debugging...")

        # Kill existing Chrome instances
        os.system("taskkill /F /IM chrome.exe >nul 2>&1")
        time.sleep(2)

        # Start Chrome with remote debugging
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if not os.path.exists(chrome_path):
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

        try:
            subprocess.Popen([
                chrome_path,
                "--remote-debugging-port=9222",
                "--disable-popup-blocking",
                "--no-first-run",
                "--no-default-browser-check"
            ])
            time.sleep(5)
            print("[OK] Chrome started with remote debugging on port 9222")
        except Exception as e:
            print(f"[ERROR] Could not start Chrome: {e}")
            return False

        return True

    def connect_to_chrome(self):
        """Connect to Chrome instance via remote debugging"""
        print("[*] Connecting to Chrome remote debugging...")

        try:
            options = Options()
            options.add_experimental_option("debuggerAddress", "localhost:9222")
            self.driver = webdriver.Chrome(options=options, service_args=['--verbose'])
            self.wait = WebDriverWait(self.driver, 20)
            self.actions = ActionChains(self.driver)
            print("[OK] Connected to Chrome")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to connect to Chrome: {e}")
            return False

    def navigate_and_login(self):
        """Navigate to Google Ads and ensure logged in"""
        print("\n[STEP 1] Navigating to Google Ads...")

        self.driver.get("https://ads.google.com/aw/conversions")
        time.sleep(3)

        # Check if login is needed
        current_url = self.driver.current_url
        if "accounts.google.com" in current_url:
            print("[!] Google login required. Please log in in the browser window.")
            input("Press Enter after you've logged in...")

            # Wait for redirect to Google Ads
            time.sleep(3)

        self.driver.get("https://ads.google.com/aw/conversions")
        time.sleep(3)

        print("[OK] On Google Ads Conversions page")
        return True

    def create_conversion(self, name, category, value, event_name):
        """Create a single conversion action"""
        print(f"\n[*] Creating conversion: {name}")

        try:
            # Click "New conversion action" button
            print("  - Clicking 'New conversion action'...")
            new_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'New conversion action')]"))
            )
            new_btn.click()
            time.sleep(2)

            # Select "Website"
            print("  - Selecting 'Website'...")
            website_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Website')]"))
            )
            website_btn.click()
            time.sleep(2)

            # Enter conversion name
            print(f"  - Entering name: {name}")
            name_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Conversion name']"))
            )
            name_input.clear()
            name_input.send_keys(name)
            time.sleep(1)

            # Select category
            print(f"  - Setting category: {category}")
            category_selects = self.driver.find_elements(By.TAG_NAME, "select")
            if category_selects:
                Select(category_selects[0]).select_by_visible_text(category)
                time.sleep(1)

            # Set value
            print(f"  - Setting value: ${value}")
            value_inputs = self.driver.find_elements(By.XPATH, "//input[@type='number']")
            if value_inputs:
                value_inputs[0].clear()
                value_inputs[0].send_keys(value)
                time.sleep(1)

            # Scroll down to see more options
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)

            # Select Google Analytics 4
            print("  - Selecting Google Analytics 4...")
            ga4_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Google Analytics 4')]"))
            )
            ga4_option.click()
            time.sleep(2)

            # Enter event name
            print(f"  - Setting event: {event_name}")
            event_inputs = self.driver.find_elements(By.XPATH, "//input[@aria-label='Event name']")
            if event_inputs:
                event_inputs[0].clear()
                event_inputs[0].send_keys(event_name)
                time.sleep(1)

            # Click "Create and continue"
            print("  - Clicking 'Create and continue'...")
            create_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Create and continue')]"))
            )
            create_btn.click()
            time.sleep(3)

            print(f"[OK] Created: {name}")
            return True

        except Exception as e:
            print(f"[ERROR] Failed to create conversion: {e}")
            self.driver.save_screenshot(f"error_create_conversion_{name}.png")
            return False

    def link_conversions_to_campaign(self, campaign_name):
        """Link conversions to a campaign"""
        print(f"\n[*] Linking conversions to: {campaign_name}")

        try:
            # Navigate to campaigns
            print("  - Going to Campaigns page...")
            self.driver.get("https://ads.google.com/aw/campaigns")
            time.sleep(3)

            # Click on campaign
            print(f"  - Clicking on campaign: {campaign_name}")
            campaign_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//a[contains(., '{campaign_name}')]"))
            )
            campaign_link.click()
            time.sleep(3)

            # Click Settings tab
            print("  - Clicking Settings tab...")
            settings_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Settings')]"))
            )
            settings_tab.click()
            time.sleep(2)

            # Scroll to find conversion actions section
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1)

            # Find and click edit for conversion actions
            print("  - Finding conversion actions section...")
            edit_btns = self.driver.find_elements(By.XPATH, "//button[@aria-label='Edit']")
            if edit_btns:
                edit_btns[0].click()  # First edit button should be for conversions
                time.sleep(2)

            # Check all conversion checkboxes
            print("  - Checking conversion action checkboxes...")
            checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            for checkbox in checkboxes[:3]:  # Check first 3 (our conversions)
                if not checkbox.is_selected():
                    checkbox.click()
                    time.sleep(0.5)

            # Click Save
            print("  - Clicking Save...")
            save_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]"))
            )
            save_btn.click()
            time.sleep(2)

            print(f"[OK] Linked to: {campaign_name}")
            return True

        except Exception as e:
            print(f"[ERROR] Failed to link conversions: {e}")
            self.driver.save_screenshot(f"error_link_campaign_{campaign_name}.png")
            return False

    def run(self):
        """Run full automation"""
        print("\n" + "=" * 70)
        print("GOOGLE ADS CONVERSION SETUP - FULL AUTOMATION".center(70))
        print("=" * 70)

        # Start Chrome
        if not self.start_chrome_with_debugging():
            return False

        # Connect to Chrome
        if not self.connect_to_chrome():
            return False

        # Navigate and login
        if not self.navigate_and_login():
            return False

        # Create conversions
        print("\n" + "=" * 70)
        print("CREATING CONVERSIONS".center(70))
        print("=" * 70)

        conversions = [
            ("Contact Form Submission", "Leads", "75", "conversion"),
            ("Resource Download", "Leads", "25", "file_download"),
            ("Page Engagement (Scroll)", "Engagement", "5", "page_engagement")
        ]

        for name, category, value, event in conversions:
            self.create_conversion(name, category, value, event)
            time.sleep(2)

        # Link conversions to campaigns
        print("\n" + "=" * 70)
        print("LINKING TO CAMPAIGNS".center(70))
        print("=" * 70)

        campaigns = [
            "Adult Autism Signs",
            "Child Autism Evaluation",
            "IEP & S"
        ]

        for campaign in campaigns:
            self.link_conversions_to_campaign(campaign)
            time.sleep(2)

        # Done
        print("\n" + "=" * 70)
        print("AUTOMATION COMPLETE!".center(70))
        print("=" * 70)
        print("\nNext steps:")
        print("  1. Google Ads page will refresh automatically")
        print("  2. Wait 5-10 minutes for changes to propagate")
        print("  3. Check campaign diagnostics - should improve")
        print("  4. Full data flow in 24-48 hours")

        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleAdsAutomation()
    automation.run()
