#!/usr/bin/env python3
"""
Email Investigator - Digital Footprint Analyzer
A legal open-source intelligence tool for analyzing email addresses and finding digital footprints.
This tool uses entirely legal methods and publicly available information.
"""

import re
import json
import os
import time
import webbrowser
from datetime import datetime

class EmailInvestigator:
    def __init__(self, email_address):
        """Initialize with an email address to investigate"""
        self.email_address = email_address.lower().strip()
        self.domain = self.email_address.split('@')[1] if '@' in self.email_address else ""
        self.username = self.email_address.split('@')[0] if '@' in self.email_address else self.email_address
        self.results = {
            "email": self.email_address,
            "domain_info": {},
            "username_analysis": {},
            "social_media": [],
            "data_breach_check_urls": [],
            "search_urls": [],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Validate email format
        if not self.is_valid_email():
            print(f"[!] Invalid email format: {self.email_address}")
            self.is_valid = False
        else:
            self.is_valid = True
    
    def is_valid_email(self):
        """Check if the email has valid format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, self.email_address))
    
    def analyze(self):
        """Run full analysis on the email"""
        if not self.is_valid:
            return self.results
            
        print(f"\n[+] Analyzing email: {self.email_address}")
        
        self.analyze_domain()
        self.analyze_username()
        self.find_social_profiles()
        self.generate_search_urls()
        self.check_data_breaches()
        
        return self.results
    
    def analyze_domain(self):
        """Analyze the email domain"""
        print(f"[+] Analyzing domain: {self.domain}")
        
        # Common mail providers
        common_providers = {
            "gmail.com": "Google",
            "yahoo.com": "Yahoo",
            "hotmail.com": "Microsoft",
            "outlook.com": "Microsoft",
            "aol.com": "AOL",
            "protonmail.com": "ProtonMail",
            "icloud.com": "Apple",
            "mail.com": "Mail.com",
            "zoho.com": "Zoho",
            "yandex.com": "Yandex",
            "rediffmail.com": "Rediff",
            "indiatimes.com": "Indiatimes"
        }
        
        # Check if it's a common provider
        provider = common_providers.get(self.domain.lower(), "Unknown")
        
        # Company domain or personal domain check (simplistic)
        domain_type = "Personal Email Provider" if provider != "Unknown" else "Possibly Company/Organization Domain"
        
        self.results["domain_info"] = {
            "domain": self.domain,
            "provider": provider,
            "type": domain_type,
            "whois_url": f"https://whois.domaintools.com/{self.domain}"
        }
    
    def analyze_username(self):
        """Analyze the username part of the email"""
        print(f"[+] Analyzing username: {self.username}")
        
        # Check for name patterns
        name_parts = re.findall(r'[a-zA-Z]+', self.username)
        
        # Check for numbers (could be birth year)
        numbers = re.findall(r'\d+', self.username)
        
        # Check common username patterns
        patterns = []
        if re.match(r'[a-zA-Z]+\.[a-zA-Z]+', self.username):
            patterns.append("firstname.lastname")
        elif re.match(r'[a-zA-Z]+_[a-zA-Z]+', self.username):
            patterns.append("firstname_lastname")
        elif len(name_parts) == 1 and numbers:
            patterns.append("name+number (possibly name+birthyear)")
        
        self.results["username_analysis"] = {
            "username": self.username,
            "possible_name_parts": name_parts,
            "numbers": numbers,
            "patterns_detected": patterns
        }
    
    def find_social_profiles(self):
        """Generate URLs to search for this email on social media"""
        print("[+] Generating social media search URLs")
        
        social_platforms = [
            {
                "name": "LinkedIn",
                "url": f"https://www.linkedin.com/pub/dir/?email={self.email_address}"
            },
            {
                "name": "Facebook",
                "url": f"https://www.facebook.com/search/top/?q={self.email_address}"
            },
            {
                "name": "Twitter",
                "url": f"https://twitter.com/search?q={self.email_address}"
            },
            {
                "name": "Instagram",
                "url": f"https://www.instagram.com/{self.username}"
            },
            {
                "name": "GitHub",
                "url": f"https://github.com/{self.username}"
            },
            {
                "name": "Medium",
                "url": f"https://medium.com/@{self.username}"
            },
            {
                "name": "Quora",
                "url": f"https://www.quora.com/profile/{self.username}"
            }
        ]
        
        self.results["social_media"] = social_platforms
    
    def check_data_breaches(self):
        """Generate URLs to check if email was in known data breaches"""
        print("[+] Generating data breach check URLs")
        
        breach_check_services = [
            {
                "name": "HaveIBeenPwned",
                "url": f"https://haveibeenpwned.com/account/{self.email_address}",
                "description": "Check if your email was in a data breach"
            },
            {
                "name": "BreachDirectory",
                "url": f"https://breachdirectory.org/{self.email_address}",
                "description": "Search for breached accounts"
            }
        ]
        
        self.results["data_breach_check_urls"] = breach_check_services
    
    def generate_search_urls(self):
        """Generate search engine URLs"""
        print("[+] Generating search engine URLs")
        
        search_engines = [
            {
                "name": "Google",
                "url": f"https://www.google.com/search?q=%22{self.email_address}%22"
            },
            {
                "name": "Google (username)",
                "url": f"https://www.google.com/search?q=%22{self.username}%22"
            },
            {
                "name": "DuckDuckGo",
                "url": f"https://duckduckgo.com/?q=%22{self.email_address}%22"
            },
            {
                "name": "Yandex",
                "url": f"https://yandex.com/search/?text=%22{self.email_address}%22"
            }
        ]
        
        self.results["search_urls"] = search_engines
    
    def open_search_pages(self):
        """Open search pages in browser"""
        if input("\n[?] Would you like to open search URLs in your browser? (y/n): ").lower() == 'y':
            # Open social profile searches
            for profile in self.results["social_media"]:
                print(f"Opening {profile['name']}...")
                webbrowser.open(profile['url'])
                time.sleep(1)  # Avoid overwhelming the browser
            
            # Open search engine results
            for search in self.results["search_urls"]:
                print(f"Opening {search['name']}...")
                webbrowser.open(search['url'])
                time.sleep(1)
    
    def save_results(self, output_dir="results"):
        """Save results to JSON file"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filename = f"{output_dir}/email_{self.email_address.replace('@', '_at_')}_{int(time.time())}.json"
        
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        
        print(f"\n[+] Results saved to {filename}")
        return filename
    
    def print_report(self):
        """Print a readable report to the console"""
        print("\n" + "="*50)
        print(f"EMAIL INVESTIGATION REPORT: {self.email_address}")
        print("="*50)
        
        print("\nBASIC INFORMATION:")
        print(f"Email: {self.email_address}")
        print(f"Username: {self.username}")
        print(f"Domain: {self.domain}")
        print(f"Provider: {self.results['domain_info'].get('provider', 'Unknown')}")
        print(f"Domain Type: {self.results['domain_info'].get('type', 'Unknown')}")
        
        print("\nUSERNAME ANALYSIS:")
        analysis = self.results["username_analysis"]
        print(f"Possible name parts: {', '.join(analysis.get('possible_name_parts', []))}")
        if analysis.get('numbers'):
            print(f"Numbers found: {', '.join(analysis.get('numbers', []))}")
        if analysis.get('patterns_detected'):
            print(f"Patterns detected: {', '.join(analysis.get('patterns_detected', []))}")
        
        print("\nSOCIAL MEDIA PROFILES TO CHECK:")
        for platform in self.results["social_media"]:
            print(f"- {platform['name']}: {platform['url']}")
        
        print("\nDATA BREACH CHECKS:")
        for service in self.results["data_breach_check_urls"]:
            print(f"- {service['name']}: {service['url']}")
        
        print("\nSEARCH ENGINE QUERIES:")
        for engine in self.results["search_urls"]:
            print(f"- {engine['name']}: {engine['url']}")
        
        print("\n" + "="*50)


if __name__ == "__main__":
    print("\n===== Email Investigator - Digital Footprint Analyzer =====")
    print("A legal OSINT tool for analyzing email addresses")
    
    email = input("\nEnter email address to investigate: ")
    investigator = EmailInvestigator(email)
    
    if investigator.is_valid:
        results = investigator.analyze()
        investigator.print_report()
        investigator.save_results()
        investigator.open_search_pages()
    else:
        print("[!] Investigation aborted due to invalid email format.")