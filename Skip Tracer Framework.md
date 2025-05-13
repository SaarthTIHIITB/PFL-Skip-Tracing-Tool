# Skip Tracer Framework

## Overview

Skip Tracer Framework is a legal Open-Source Intelligence (OSINT) toolkit designed to assist in finding public information about individuals based on various identifiers. The framework focuses on legal methods and publicly available information to conduct digital investigations.

## Components

The framework consists of four main Python scripts:

1. **skip_tracer_framework.py** - The main integration tool that orchestrates all investigations
2. **email_investigator.py** - Tool for analyzing email addresses and finding associated digital footprints
3. **phone_investigator.py** - Tool specialized for analyzing Indian phone numbers
4. **name_investigator.py** - Tool for searching people based on their names

## Features

### Email Investigation

- Email format validation
- Domain and provider analysis
- Username pattern detection
- Social media profile discovery
- Data breach search links
- Search engine query generation

### Phone Investigation (Indian Numbers)

- Number format validation and normalization
- Carrier and telecom circle identification
- Messaging platform registration checks (WhatsApp, Telegram, Signal)
- Caller ID service lookups (Truecaller, Showcaller, Eyecon)
- Search engine query generation

### Name Investigation

- Parsing name components (first, middle, last name)
- Social media profile discovery
- Professional profile search
- General search engine queries
- India-specific resources (Justdial, Electoral Search, etc.)

### Framework Integration

- Case management system
- Combined investigation capabilities
- Report generation
- Note-taking functionality
- Results saving in JSON format

## Installation

### Prerequisites

- Python 3.6 or higher
- Internet connection for web searches

### Setup

1. Clone or download all four Python files to the same directory:
   
   - skip_tracer_framework.py
   - email_investigator.py
   - phone_investigator.py
   - name_investigator.py

2. Make the files executable (Linux/Mac):
   
   bash
   
   ```bash
   chmod +x skip_tracer_framework.py email_investigator.py phone_investigator.py name_investigator.py
   ```

3. Run the main framework:
   
   bash
   
   ```bash
   python skip_tracer_framework.py
   ```
   
   or
   
   bash
   
   ```bash
   ./skip_tracer_framework.py
   ```

## Usage

### Main Menu

The framework provides a text-based menu with the following options:

1. Create New Case
2. Email Investigation
3. Phone Investigation
4. Name Investigation
5. Run All Investigations
6. Add Note to Case
7. Generate Case Report
8. Exit

### Creating a Case

Start by creating a case and entering any known information about the target:

- Full Name
- Email Address
- Phone Number
- Location

You only need to provide at least one identifier (name, email, or phone).

### Running Investigations

You can run individual investigations or all available investigations at once. Each investigation:

1. Analyzes the provided identifier
2. Generates search URLs
3. Offers to open these URLs in your browser
4. Saves results to a JSON file
5. Updates the case file with investigation results

### Adding Notes

You can add notes to the case to document findings or observations.

### Generating Reports

The framework can generate a comprehensive report summarizing all investigations in the case.

## Output

- All results are saved in a "results" directory
- Individual investigation results are stored as JSON files
- A case file (JSON) maintains the overall investigation state

## Legal and Ethical Use

This framework is designed for legal OSINT activities only. It:

- Uses only publicly available information
- Does not perform any hacking or unauthorized access
- Does not store personal data beyond the local JSON files
- Should be used in accordance with local privacy laws

## Limitations

- Phone investigation is optimized for Indian numbers
- Carrier identification is limited to a sample database
- Social media and platform checks only generate URLs, they don't verify account existence
- Location-based searches are simplistic and may not be accurate

## Extending the Framework

You can extend this framework by:

1. Adding new investigation modules
2. Expanding the carrier database for more accurate phone analysis
3. Implementing more sophisticated name parsing algorithms
4. Adding data visualization capabilities
5. Implementing database storage instead of JSON files

## License

This software is meant for legitimate investigative purposes only.

---

*Note: This framework is designed for legitimate skip tracing and OSINT research activities. Always respect privacy laws and use this tool ethically and responsibly.*
