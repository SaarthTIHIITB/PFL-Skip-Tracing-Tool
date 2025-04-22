#!/usr/bin/env python3
"""
Skip Tracer Framework - Main Integration Tool
A legal OSINT framework for skip tracing individuals in India.
This tool integrates email, phone, and name investigation modules.
"""

import os
import sys
import json
import time
from datetime import datetime

# Import the individual investigators
try:
    from email_investigator import EmailInvestigator
    from phone_investigator import PhoneInvestigator
    from name_investigator import NameInvestigator
except ImportError:
    print("[!] Error: Required module not found.")
    print("[i] Make sure email_investigator.py, phone_investigator.py, and name_investigator.py")
    print("    are in the same directory as this script.")
    sys.exit(1)

class SkipTracerFramework:
    def __init__(self):
        """Initialize the framework"""
        self.case_data = {
            "case_id": f"case_{int(time.time())}",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "target_info": {},
            "investigations": {
                "email": [],
                "phone": [],
                "name": []
            },
            "notes": []
        }
        
        self.results_dir = "results"
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def create_case(self):
        """Create a new investigation case"""
        print("\n" + "="*50)
        print("CREATE NEW INVESTIGATION CASE")
        print("="*50)
        
        print("\nEnter known information about the target (leave blank if unknown):")
        name = input("Full Name: ")
        email = input("Email Address: ")
        phone = input("Phone Number: ")
        location = input("Location: ")
        
        if not any([name, email, phone]):
            print("[!] Error: At least one identifier (name, email, or phone) is required.")
            return False
        
        self.case_data["target_info"] = {
            "name": name,
            "email": email,
            "phone": phone,
            "location": location
        }
        
        self.save_case()
        print(f"\n[+] Case created with ID: {self.case_data['case_id']}")
        return True
    
    def investigate_email(self):
        """Run email investigation"""
        if not self.case_data["target_info"].get("email") and not self.prompt_for_email():
            return
        
        email = self.case_data["target_info"]["email"]
        print(f"\n[+] Running email investigation for: {email}")
        
        investigator = EmailInvestigator(email)
        if investigator.is_valid:
            results = investigator.analyze()
            investigator.print_report()
            result_file = investigator.save_results(self.results_dir)
            
            # Store results in case
            self.case_data["investigations"]["email"].append({
                "email": email,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "result_file": result_file,
                "summary": {
                    "domain": results["domain_info"].get("domain", "Unknown"),
                    "provider": results["domain_info"].get("provider", "Unknown"),
                    "username": results["username_analysis"].get("username", "Unknown")
                }
            })
            
            investigator.open_search_pages()
            self.save_case()
    
    def investigate_phone(self):
        """Run phone investigation"""
        if not self.case_data["target_info"].get("phone") and not self.prompt_for_phone():
            return
        
        phone = self.case_data["target_info"]["phone"]
        print(f"\n[+] Running phone investigation for: {phone}")
        
        investigator = PhoneInvestigator(phone)
        if investigator.is_valid:
            results = investigator.analyze()
            investigator.print_report()
            result_file = investigator.save_results(self.results_dir)
            
            # Store results in case
            self.case_data["investigations"]["phone"].append({
                "phone": phone,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "result_file": result_file,
                "summary": {
                    "carrier": results["carrier_info"].get("carrier", "Unknown"),
                    "circle": results["carrier_info"].get("circle", "Unknown"),
                    "normalized_number": results["normalized_number"]
                }
            })
            
            investigator.open_search_pages()
            self.save_case()
    
    def investigate_name(self):
        """Run name investigation"""
        if not self.case_data["target_info"].get("name") and not self.prompt_for_name():
            return
        
        name = self.case_data["target_info"]["name"]
        location = self.case_data["target_info"].get("location", None)
        
        print(f"\n[+] Running name investigation for: {name}")
        
        investigator = NameInvestigator(name, location)
        if investigator.is_valid:
            results = investigator.analyze()
            investigator.print_report()
            result_file = investigator.save_results(self.results_dir)
            
            # Store results in case
            self.case_data["investigations"]["name"].append({
                "name": name,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "result_file": result_file,
                "summary": {
                    "first_name": results["components"].get("first_name", "Unknown"),
                    "last_name": results["components"].get("last_name", "Unknown"),
                    "location": location
                }
            })
            
            investigator.open_search_pages()
            self.save_case()
    
    def run_all_investigations(self):
        """Run all available investigations"""
        print("\n[+] Running all available investigations")
        
        if self.case_data["target_info"].get("email"):
            self.investigate_email()
        
        if self.case_data["target_info"].get("phone"):
            self.investigate_phone()
        
        if self.case_data["target_info"].get("name"):
            self.investigate_name()
    
    def prompt_for_email(self):
        """Prompt for email if not available"""
        email = input("\nEnter email address to investigate: ")
        if email:
            self.case_data["target_info"]["email"] = email
            return True
        return False
    
    def prompt_for_phone(self):
        """Prompt for phone if not available"""
        phone = input("\nEnter phone number to investigate: ")
        if phone:
            self.case_data["target_info"]["phone"] = phone
            return True
        return False
    
    def prompt_for_name(self):
        """Prompt for name if not available"""
        name = input("\nEnter full name to investigate: ")
        if name:
            self.case_data["target_info"]["name"] = name
            location = input("Enter location (optional, press Enter to skip): ")
            if location:
                self.case_data["target_info"]["location"] = location
            return True
        return False
    
    def add_note(self):
        """Add a note to the case"""
        note = input("\nEnter your note: ")
        if note:
            self.case_data["notes"].append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "content": note
            })
            self.save_case()
            print("[+] Note added to the case")
    
    def save_case(self):
        """Save the case data to a JSON file"""
        case_file = f"{self.results_dir}/{self.case_data['case_id']}.json"
        
        with open(case_file, 'w') as f:
            json.dump(self.case_data, f, indent=4)
        
        return case_file
    
    def generate_report(self):
        """Generate a comprehensive report of all investigations"""
        print("\n" + "="*50)
        print(f"CASE REPORT: {self.case_data['case_id']}")
        print("="*50)
        
        print("\nTARGET INFORMATION:")
        target = self.case_data["target_info"]
        for key, value in target.items():
            if value:
                print(f"{key.capitalize()}: {value}")
        
        print("\nINVESTIGATION SUMMARY:")
        
        # Email investigations
        if self.case_data["investigations"]["email"]:
            print("\nEmail Investigations:")
            for i, inv in enumerate(self.case_data["investigations"]["email"], 1):
                print(f"  {i}. {inv['email']} ({inv['timestamp']})")
                for key, value in inv["summary"].items():
                    print(f"     - {key.capitalize()}: {value}")
        
        # Phone investigations
        if self.case_data["investigations"]["phone"]:
            print("\nPhone Investigations:")
            for i, inv in enumerate(self.case_data["investigations"]["phone"], 1):
                print(f"  {i}. {inv['phone']} ({inv['timestamp']})")
                for key, value in inv["summary"].items():
                    print(f"     - {key.capitalize()}: {value}")
        
        # Name investigations
        if self.case_data["investigations"]["name"]:
            print("\nName Investigations:")
            for i, inv in enumerate(self.case_data["investigations"]["name"], 1):
                print(f"  {i}. {inv['name']} ({inv['timestamp']})")
                for key, value in inv["summary"].items():
                    if value:
                        print(f"     - {key.capitalize()}: {value}")
        
        # Notes
        if self.case_data["notes"]:
            print("\nCase Notes:")
            for i, note in enumerate(self.case_data["notes"], 1):
                print(f"  {i}. {note['timestamp']}: {note['content']}")
        
        print("\nReport Files:")
        report_files = []
        
        for category in ["email", "phone", "name"]:
            for inv in self.case_data["investigations"][category]:
                if "result_file" in inv:
                    report_files.append(inv["result_file"])
        
        for i, file in enumerate(report_files, 1):
            print(f"  {i}. {file}")
        
        print("\n" + "="*50)
    
    def display_menu(self):
        """Display the main menu"""
        while True:
            print("\n" + "="*50)
            print("SKIP TRACER FRAMEWORK - MAIN MENU")
            print("="*50)
            print("1. Create New Case")
            print("2. Email Investigation")
            print("3. Phone Investigation")
            print("4. Name Investigation")
            print("5. Run All Investigations")
            print("6. Add Note to Case")
            print("7. Generate Case Report")
            print("8. Exit")
            
            choice = input("\nEnter your choice (1-8): ")
            
            if choice == "1":
                self.create_case()
            elif choice == "2":
                self.investigate_email()
            elif choice == "3":
                self.investigate_phone()
            elif choice == "4":
                self.investigate_name()
            elif choice == "5":
                self.run_all_investigations()
            elif choice == "6":
                self.add_note()
            elif choice == "7":
                self.generate_report()
            elif choice == "8":
                print("\n[+] Exiting Skip Tracer Framework. Goodbye!")
                sys.exit(0)
            else:
                print("[!] Invalid choice. Please try again.")


if __name__ == "__main__":
    print("\n" + "="*70)
    print("SKIP TRACER FRAMEWORK - DIGITAL FOOTPRINT ANALYZER")
    print("A legal OSINT tool for skip tracing individuals in India")
    print("="*70)
    
    framework = SkipTracerFramework()
    framework.display_menu()