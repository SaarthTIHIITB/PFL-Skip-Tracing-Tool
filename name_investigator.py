#!/usr/bin/env python3
"""
Name Investigator - Person Search Tool
A legal open-source intelligence (OSINT) tool for finding people based on their names.
Uses publicly available and legal search methods.
"""

import re
import json
import os
import time
import webbrowser
from datetime import datetime

class NameInvestigator:
    def __init__(self, full_name, location=None, age=None):
        self.full_name = full_name.strip()
        self.location = location.strip() if location else None
        self.age = age

        # Parse name components
        name_parts = self.full_name.split()
        self.first_name = name_parts[0] if len(name_parts) >= 1 else ""
        self.last_name = name_parts[-1] if len(name_parts) >= 2 else ""
        self.middle_name = ' '.join(name_parts[1:-1]) if len(name_parts) > 2 else None

        self.results = {
            "name": self.full_name,
            "components": {
                "first_name": self.first_name,
                "middle_name": self.middle_name,
                "last_name": self.last_name
            },
            "location": self.location,
            "age": self.age,
            "social_media_searches": [],
            "professional_searches": [],
            "general_searches": [],
            "india_specific_searches": [],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.is_valid = self.is_valid_name()
        if not self.is_valid:
            print(f"[!] Invalid name format: {self.full_name}")

    def is_valid_name(self):
        """Check if the name contains valid characters"""
        return bool(re.match(r'^[A-Za-z\s.\'-]+$', self.full_name)) and len(self.full_name) > 1

    def analyze(self):
        """Run full analysis on the name"""
        if not self.is_valid:
            return self.results

        print(f"\n[+] Analyzing name: {self.full_name}")
        self.generate_social_media_searches()
        self.generate_professional_searches()
        self.generate_general_searches()
        self.generate_india_specific_searches()
        return self.results

    def generate_social_media_searches(self):
        """Generate URLs to search on social media platforms"""
        print("[+] Generating social media search URLs")

        encoded_name = self.full_name.replace(" ", "%20")
        platforms = [
            {"name": "Facebook", "url": f"https://www.facebook.com/search/people/?q={encoded_name}"},
            {"name": "LinkedIn", "url": f"https://www.linkedin.com/search/results/people/?keywords={encoded_name}"},
            {"name": "Twitter", "url": f"https://twitter.com/search?q={encoded_name}&f=user"},
            {"name": "Instagram", "url": f"https://www.instagram.com/{self.first_name.lower()}{self.last_name.lower()}"},
            {"name": "Instagram Search", "url": f"https://www.google.com/search?q=site%3Ainstagram.com+%22{encoded_name}%22"},
            {"name": "YouTube", "url": f"https://www.youtube.com/results?search_query={encoded_name}"},
            {"name": "Reddit", "url": f"https://www.reddit.com/search/?q={encoded_name}&type=user"},
            {"name": "GitHub", "url": f"https://github.com/search?q={encoded_name}&type=users"}
        ]

        if self.location:
            encoded_location = self.location.replace(" ", "%20")
            platforms.append({
                "name": "Facebook (with location)",
                "url": f"https://www.facebook.com/search/people/?q={encoded_name}&city={encoded_location}"
            })
            platforms.append({
                "name": "LinkedIn (with location)",
                "url": f"https://www.linkedin.com/search/results/people/?keywords={encoded_name}&geoUrn=%5B%22{encoded_location}%22%5D"
            })

        self.results["social_media_searches"] = platforms

    def generate_professional_searches(self):
        """Generate URLs to search on professional databases"""
        print("[+] Generating professional search URLs")

        encoded_name = self.full_name.replace(" ", "%20")
        professional_sites = [
            {"name": "LinkedIn", "url": f"https://www.linkedin.com/search/results/people/?keywords={encoded_name}"},
            {"name": "Naukri", "url": f"https://www.naukri.com/mnjuser/profile?id={encoded_name}"},
            {"name": "TimesJobs", "url": f"https://www.timesjobs.com/candidate/resume-search.html?searchType=personalizedSearch&from=submit&txtKeywords={encoded_name}"},
            {"name": "Google Scholar", "url": f"https://scholar.google.com/scholar?q=author%3A%22{encoded_name}%22"}
        ]

        if self.location:
            encoded_location = self.location.replace(" ", "%20")
            professional_sites.append({
                "name": "LinkedIn (with location)",
                "url": f"https://www.linkedin.com/search/results/people/?keywords={encoded_name}&geoUrn=%5B%22{encoded_location}%22%5D"
            })
            professional_sites.append({
                "name": "Naukri (with location)",
                "url": f"https://www.naukri.com/mnjuser/profile?id={encoded_name}&locname={encoded_location}"
            })

        self.results["professional_searches"] = professional_sites

    def generate_general_searches(self):
        """Generate URLs for general search engines"""
        print("[+] Generating general search URLs")

        encoded_name = self.full_name.replace(" ", "%20")
        search_engines = [
            {"name": "Google", "url": f"https://www.google.com/search?q=%22{encoded_name}%22"},
            {"name": "Bing", "url": f"https://www.bing.com/search?q=%22{encoded_name}%22"},
            {"name": "DuckDuckGo", "url": f"https://duckduckgo.com/?q=%22{encoded_name}%22"},
            {"name": "Yandex", "url": f"https://yandex.com/search/?text=%22{encoded_name}%22"}
        ]

        if self.location:
            encoded_location = self.location.replace(" ", "%20")
            search_engines.append({
                "name": "Google (with location)",
                "url": f"https://www.google.com/search?q=%22{encoded_name}%22+%22{encoded_location}%22"
            })

        self.results["general_searches"] = search_engines

    def generate_india_specific_searches(self):
        """Generate URLs for India-specific resources"""
        print("[+] Generating India-specific search URLs")

        encoded_name = self.full_name.replace(" ", "%20")
        india_sites = [
            {"name": "Justdial", "url": f"https://www.justdial.com/searchresult.php?srchname={encoded_name}"},
            {"name": "Truecaller (Google search)", "url": f"https://www.google.com/search?q=site%3Atruecaller.com+%22{encoded_name}%22"},
            {"name": "Electoral Search", "url": "https://electoralsearch.in/", "description": "Search for voter information (manual input)"},
            {"name": "Ministry of Corporate Affairs", "url": "https://www.mca.gov.in/mcafoportal/viewDirectorMasterData.do", "description": "Search for company directors (manual input)"}
        ]

        if self.location:
            encoded_location = self.location.replace(" ", "%20")
            india_sites.append({
                "name": "Justdial (with location)",
                "url": f"https://www.justdial.com/{encoded_location}/search?q={encoded_name}"
            })

        self.results["india_specific_searches"] = india_sites

    def open_search_pages(self):
        """Prompt user to open search URLs"""
        if input("\n[?] Would you like to open search URLs in your browser? (y/n): ").lower() == 'y':
            categories = [
                ("Social Media", self.results["social_media_searches"]),
                ("Professional Profiles", self.results["professional_searches"]),
                ("General Searches", self.results["general_searches"]),
                ("India-Specific Resources", self.results["india_specific_searches"])
            ]
            for category_name, urls in categories:
                if input(f"[?] Open {category_name}? (y/n): ").lower() == 'y':
                    for site in urls:
                        print(f"Opening {site['name']}...")
                        webbrowser.open(site['url'])
                        time.sleep(1)

    def save_results(self, output_dir="results"):
        """Save results to JSON"""
        os.makedirs(output_dir, exist_ok=True)
        filename = f"{output_dir}/name_{self.full_name.lower().replace(' ', '_')}_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)
        print(f"[+] Results saved to {filename}")
        return filename

    def print_report(self):
        """Print the investigation report"""
        print("\n" + "="*50)
        print(f"NAME INVESTIGATION REPORT: {self.full_name}")
        print("="*50)

        print("\nBASIC INFORMATION:")
        print(f"Full Name: {self.full_name}")
        print(f"First Name: {self.first_name}")
        if self.middle_name:
            print(f"Middle Name: {self.middle_name}")
        print(f"Last Name: {self.last_name}")
        if self.location:
            print(f"Location: {self.location}")
        if self.age:
            print(f"Age: {self.age}")

        for section, links in [
            ("SOCIAL MEDIA PROFILES TO CHECK", "social_media_searches"),
            ("PROFESSIONAL PROFILES TO CHECK", "professional_searches"),
            ("GENERAL SEARCH QUERIES", "general_searches"),
            ("INDIA-SPECIFIC RESOURCES", "india_specific_searches")
        ]:
            print(f"\n{section}:")
            for site in self.results[links]:
                desc = f" - {site.get('description')}" if 'description' in site else ""
                print(f"- {site['name']}: {site['url']}{desc}")

        print("\n" + "="*50)

if __name__ == "__main__":
    print("\n===== Name Investigator - Person Search Tool =====")
    name = input("\nEnter full name to investigate: ").strip()
    location = input("Enter location (optional, press Enter to skip): ").strip() or None
    age_input = input("Enter age (optional, press Enter to skip): ").strip()
    age = int(age_input) if age_input.isdigit() else None

    investigator = NameInvestigator(name, location, age)
    if investigator.is_valid:
        investigator.analyze()
        investigator.print_report()
        investigator.save_results()
        investigator.open_search_pages()
    else:
        print("[!] Investigation aborted due to invalid name format.")
