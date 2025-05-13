# PFL-Skip-Tracing-Tool

## Skip Tracing tool for PFL applications/PFL Collections
### Implementation of Skip Tracer Framework for Locating Individuals Based on Email, Name, and Phone Number
### Objective:
To outline the steps taken to implement the Skip Tracer Framework, a tool designed to track individuals using publicly available information, such as email addresses, phone numbers, and names. The primary goal is to locate people who have taken loans from Non-Banking Financial Companies (NBFCs) but are now untraceable. This solution is built using legal methods and focuses on open-source intelligence (OSINT), ensuring compliance with privacy laws and regulations.
Tools and Technologies Used:
Python 3.6+: The framework is built using Python, offering flexibility and compatibility for future upgrades.

OSINT tools and AI-powered techniques that adhere to all legal standards. These methods include API calls to popular social media and messaging platforms.

### Libraries/Tools:
webbrowser: Used to open search URLs directly in the browser.
JSON: For storing and exporting investigation results.
APIs from platforms such as LinkedIn, Facebook, Instagram, WhatsApp, and TrueCaller.

### System Setup:
Clone and Install the Skip Tracer Framework: To get started, the framework needs to be downloaded or cloned from the repository, which includes the following scripts:

email_investigator.py

phone_investigator.py

name_investigator.py

skip_tracer_framework.py

### Setting Up the Virtual Environment: Setting up a virtual environment is highly recommended to keep dependencies isolated:
~~~
  mkdir skip_tracer
  cd skip_tracer
  python -m venv venv  
~~~
### Activate virtual environment
~~~
venv\Scripts\activate (Windows)
source venv/bin/activate (macOS/Linux)
~~~
### Installing Necessary Dependencies: Once the virtual environment is set up, you need to install the required dependencies:
~~~
pip install webbrowser
~~~

### How the Framework Works:
The Skip Tracer Framework is divided into three main modules. Each module is designed to investigate a specific piece of information—email address, phone number, or full name—and find any relevant details linked to the target.
#### Email Investigation (email_investigator.py):

Purpose: Locate an individual using their email address.

How It Works: The tool analyzes the domain of the email (e.g., Gmail, Yahoo) and looks for any associated social media accounts. It also checks if the email has been part of any data breaches.

Tools/Platforms Used: LinkedIn, Instagram, Facebook, Gmail, Yahoo.

Output: The result includes links to the person’s social media profiles, domain information, and any data breaches associated with the email.

#### Phone Number Investigation (phone_investigator.py):

Purpose: Find an individual based on their phone number.

How It Works: The tool examines the phone number’s prefix to identify the carrier and geographical region. It also checks for the phone number’s registration on popular messaging platforms like WhatsApp and TrueCaller.

Tools/Platforms Used: TrueCaller, WhatsApp, Telegram.

Output: The tool provides the carrier information, links to messaging platforms, and any public records associated with the number.

#### Name Investigation (name_investigator.py):

Purpose: Search for an individual based on their full name.

How It Works: This tool splits the name into its components (first, middle, and last) and searches for matching profiles across social media platforms like LinkedIn, Facebook, and Instagram.

Tools/Platforms Used: LinkedIn, Facebook, Instagram.

Output: Provides links to any profiles or public information found on these platforms.

#### Integrated Framework (skip_tracer_framework.py):

Purpose: Manage and run investigations in a centralized manner.

How It Works: The framework allows you to input any available identifiers (email, phone number, or name) and select which investigations you’d like to run. It stores results in JSON files and can generate comprehensive reports.

### Key Features:

Case creation and management

Selective or all investigations at once

Detailed report generation, including case notes and investigation findings

### Investigation Process:
#### Email Investigation:

Goal: Identify any public profiles tied to an email address.

How: The tool looks at the domain of the email, searches for matching profiles, and checks if the email is linked to any data breaches.

Platforms Used: LinkedIn, Instagram, Facebook, Google search.

Outcome: It generates a list of social media profiles and public information related to the email.

#### Phone Number Investigation:

Goal: Trace the owner of a phone number.

How: The tool identifies the carrier and region based on the phone number’s prefix and checks for registration on messaging apps like WhatsApp and TrueCaller.

Platforms Used: TrueCaller, WhatsApp, Telegram.

Outcome: The result provides the carrier details, as well as links to platforms like WhatsApp where the number might be registered.

#### Name Investigation:

Goal: Find social media or professional profiles linked to a name.

How: The tool splits the full name into components and searches for those components on social platforms.

Platforms Used: LinkedIn, Facebook, Instagram.

Outcome: The tool returns links to profiles or relevant public records associated with the name.

#### Integrated Framework:

Goal: Run all investigations and generate a full report.

How: Users input identifiers such as email, phone number, or name, select the type of investigation, and generate a report that compiles all findings.

Outcome: The report includes a summary of the investigation, case notes, and any relevant digital footprints found.

### Respect for Privacy: The tool does not scrape private data (avoids webscraping) or violate any privacy laws.

### Legitimate Use: The framework is meant for finding missing persons, verifying identities for legal purposes, or reconnecting with individuals for legitimate reasons.

### Conclusion:
The results are good enough to begin with and can be improved upon. All the resources used are free and legal. Few results are unreliable, but with more research and improvement or using paid APIs like Pipl, Hunter.io, Fullcontact, zerobounce, etc. it can be improved.

To access APIs and using access tokens from Meta, Google directly is tedious and doesn’t provide very reliable results.

#### GitHub link for codes: https://github.com/SaarthTIHIITB/PFL-Skip-Tracing-Tool.git
#### More info and research: https://docs.google.com/document/d/11q2E4N4BkfxtRMINN0NzKW_XP1aomlyWh-xBx5hU9XQ/edit?tab=t.0
