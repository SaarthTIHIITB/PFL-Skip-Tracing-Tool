#!/usr/bin/env python3
"""
Phone Number Investigator - Indian Numbers Analysis
A legal open-source intelligence tool for analyzing Indian phone numbers and finding digital footprints.
This tool uses entirely legal methods and publicly available information.
"""

import re
import json
import os
import time
import webbrowser
from datetime import datetime

class PhoneInvestigator:
    def __init__(self, phone_number):
        """Initialize with a phone number to investigate"""
        # Clean the phone number
        self.raw_number = phone_number
        self.phone_number = re.sub(r'[^0-9]', '', phone_number)
        
        # Format for India (remove leading country code if present)
        if self.phone_number.startswith('91') and len(self.phone_number) > 10:
            self.phone_number = self.phone_number[2:]
        
        # Store results
        self.results = {
            "raw_input": self.raw_number,
            "normalized_number": self.phone_number,
            "full_number_with_code": f"+91{self.phone_number}" if len(self.phone_number) == 10 else self.phone_number,
            "carrier_info": {},
            "search_urls": [],
            "messaging_platforms": [],
            "caller_id_services": [],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Validate phone number
        if not self.is_valid_indian_number():
            print(f"[!] Invalid Indian phone number format: {self.phone_number}")
            self.is_valid = False
        else:
            self.is_valid = True
    
    def is_valid_indian_number(self):
        """Check if the number matches Indian mobile number format (10 digits starting with 6-9)"""
        return bool(re.match(r'^[6-9]\d{9}$', self.phone_number))
    
    def analyze(self):
        """Run full analysis on the phone number"""
        if not self.is_valid:
            return self.results
            
        print(f"\n[+] Analyzing phone number: +91 {self.phone_number}")
        
        self.identify_carrier()
        self.check_messaging_platforms()
        self.check_caller_id_services()
        self.generate_search_urls()
        
        return self.results
    
    def identify_carrier(self):
        """Identify the likely carrier based on number prefix"""
        print(f"[+] Identifying carrier information")
        
        # First 4 digits can help identify carrier and circle (simplified example)
        prefix = self.phone_number[:4]
        
        # This is a simplified mapping - a complete version would have hundreds of entries
        # These are examples and may not be 100% accurate
        carrier_prefixes = {
            # Jio prefixes
            "7000": {"carrier": "Jio", "circle": "Andhra Pradesh"},
            "7016": {"carrier": "Jio", "circle": "Bihar"},
            "7021": {"carrier": "Jio", "circle": "Delhi"},
            "7208": {"carrier": "Jio", "circle": "Maharashtra"},
            "7259": {"carrier": "Jio", "circle": "Karnataka"},
            "7276": {"carrier": "Jio", "circle": "Rajasthan"},
            "7283": {"carrier": "Jio", "circle": "Tamil Nadu"},
            "7291": {"carrier": "Jio", "circle": "Uttar Pradesh East"},
            
            # Airtel prefixes
            "8010": {"carrier": "Airtel", "circle": "Delhi"},
            "8050": {"carrier": "Airtel", "circle": "Karnataka"},
            "8072": {"carrier": "Airtel", "circle": "Tamil Nadu"},
            "8076": {"carrier": "Airtel", "circle": "UP East"},
            "8091": {"carrier": "Airtel", "circle": "Rajasthan"},
            "8095": {"carrier": "Airtel", "circle": "Kerala"},
            
            # Vodafone-Idea prefixes
            "9000": {"carrier": "Vodafone-Idea", "circle": "Andhra Pradesh"},
            "9020": {"carrier": "Vodafone-Idea", "circle": "Delhi"},
            "9036": {"carrier": "Vodafone-Idea", "circle": "Karnataka"},
            "9087": {"carrier": "Vodafone-Idea", "circle": "Tamil Nadu"},
            "9096": {"carrier": "Vodafone-Idea", "circle": "Maharashtra"}
        }
        
        # Simplified carrier identification based on first digit
        first_digit = self.phone_number[0]
        likely_carriers = {
            "6": ["Jio"],
            "7": ["Idea", "Aircel", "Jio"],
            "8": ["Airtel", "Vodafone", "Reliance"],
            "9": ["Airtel", "Vodafone", "Idea", "BSNL", "MTNL"]
        }
        
        carrier_info = carrier_prefixes.get(prefix, None)
        if carrier_info:
            self.results["carrier_info"] = carrier_info
        else:
            self.results["carrier_info"] = {
                "carrier": "Unknown",
                "circle": "Unknown",
                "possible_carriers": likely_carriers.get(first_digit, ["Unknown"])
            }
            
        # Add telecom regulatory info
        self.results["carrier_info"]["trai_dnd_url"] = "https://trai.gov.in/consumer-info/telecom/dnd-registration"
    
    def check_messaging_platforms(self):
        """Generate URLs to check number on messaging platforms"""
        print("[+] Generating messaging platform check URLs")
        
        platforms = [
            {
                "name": "WhatsApp",
                "url": f"https://wa.me/91{self.phone_number}",
                "description": "Check if number is registered on WhatsApp"
            },
            {
                "name": "Telegram",
                "url": f"https://t.me/+91{self.phone_number}",
                "description": "Open Telegram chat if number is registered"
            },
            {
                "name": "Signal (QR code)",
                "url": f"https://signal.me/#p/+91{self.phone_number}",
                "description": "Generate Signal QR code for the number"
            }
        ]
        
        self.results["messaging_platforms"] = platforms
    
    def check_caller_id_services(self):
        """Generate URLs to check number on caller ID services"""
        print("[+] Generating caller ID service check URLs")
        
        services = [
            {
                "name": "Truecaller",
                "url": f"https://www.truecaller.com/search/in/{self.phone_number}",
                "description": "Look up the number on Truecaller"
            },
            {
                "name": "Showcaller",
                "url": f"https://showcaller.app",
                "description": "Copy number to check on Showcaller app"
            },
            {
                "name": "Eyecon",
                "url": f"https://app.eyecon-app.com",
                "description": "Copy number to check on Eyecon app"
            }
        ]
        
        self.results["caller_id_services"] = services
    
    def generate_search_urls(self):
        """Generate search engine URLs"""
        print("[+] Generating search engine URLs")
        
        search_engines = [
            {
                "name": "Google",
                "url": f"https://www.google.com/search?q=%22{self.phone_number}%22"
            },
            {
                "name": "Google (with country code)",
                "url": f"https://www.google.com/search?q=%22%2B91{self.phone_number}%22"
            },
            {
                "name": "DuckDuckGo",
                "url": f"https://duckduckgo.com/?q=%22{self.phone_number}%22"
            },
            {
                "name": "Yandex",
                "url": f"https://yandex.com/search/?text=%22{self.phone_number}%22"
            }
        ]
        
        self.results["search_urls"] = search_engines
    
    def open_search_pages(self):
        """Open search pages in browser"""
        if input("\n[?] Would you like to open search URLs in your browser? (y/n): ").lower() == 'y':
            # Open caller ID services
            for service in self.results["caller_id_services"]:
                print(f"Opening {service['name']}...")
                webbrowser.open(service['url'])
                time.sleep(1)  # Avoid overwhelming the browser
            
            # Open messaging platform checks
            for platform in self.results["messaging_platforms"]:
                if input(f"\n[?] Open {platform['name']} check? (y/n): ").lower() == 'y':
                    print(f"Opening {platform['name']}...")
                    webbrowser.open(platform['url'])
                    time.sleep(1)
            
            # Open search engine results
            for search in self.results["search_urls"]:
                print(f"Opening {search['name']}...")
                webbrowser.open(search['url'])
                time.sleep(1)
    
    def save_results(self, output_dir="results"):
        """Save results to JSON file"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f"{output_dir}/phone_{self.phone_number}_{int(time.time())}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        
        print(f"\n[+] Results saved to {filename}")
        return filename
    
    def print_report(self):
        """Print a readable report to the console"""
        print("\n" + "="*50)
        print(f"PHONE NUMBER INVESTIGATION REPORT: +91 {self.phone_number}")
        print("="*50)
        
        print("\nBASIC INFORMATION:")
        print(f"Phone Number: +91 {self.phone_number}")
        
        carrier = self.results["carrier_info"]
        print("\nCARRIER INFORMATION:")
        if carrier.get("carrier") != "Unknown":
            print(f"Likely Carrier: {carrier.get('carrier', 'Unknown')}")
            print(f"Telecom Circle: {carrier.get('circle', 'Unknown')}")
        else:
            print(f"Possible Carriers: {', '.join(carrier.get('possible_carriers', ['Unknown']))}")
        
        print("\nMESSAGING PLATFORMS TO CHECK:")
        for platform in self.results["messaging_platforms"]:
            print(f"- {platform['name']}: {platform['url']}")
        
        print("\nCALLER ID SERVICES:")
        for service in self.results["caller_id_services"]:
            print(f"- {service['name']}: {service['url']}")
        
        print("\nSEARCH ENGINE QUERIES:")
        for engine in self.results["search_urls"]:
            print(f"- {engine['name']}: {engine['url']}")
        
        print("\n" + "="*50)


if __name__ == "__main__":
    print("\n===== Phone Number Investigator - Indian Numbers Analysis =====")
    print("A legal OSINT tool for analyzing Indian phone numbers")
    
    phone = input("\nEnter phone number to investigate (with or without country code): ")
    investigator = PhoneInvestigator(phone)
    
    if investigator.is_valid:
        results = investigator.analyze()
        investigator.print_report()
        investigator.save_results()
        investigator.open_search_pages()
    else:
        print("[!] Investigation aborted due to invalid phone number format.")
        print("[i] Indian mobile numbers should be 10 digits starting with 6, 7, 8, or 9.")