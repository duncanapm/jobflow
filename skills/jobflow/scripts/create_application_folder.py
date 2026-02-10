#!/usr/bin/env python3
"""
Helper script to create a new application folder with standard structure.
"""
import os
import sys
from pathlib import Path
from datetime import datetime

def slugify(text):
    """Convert text to a safe folder name."""
    return text.lower().replace(' ', '-').replace('/', '-')

def create_application_folder(applications_dir, company, position):
    """Create a folder for a new job application."""
    folder_name = f"{slugify(company)}-{slugify(position)}"
    folder_path = Path(applications_dir) / folder_name

    # Create folder
    folder_path.mkdir(parents=True, exist_ok=True)

    # Create standard files
    files_to_create = {
        "job-description.txt": f"""Job Description for {position} at {company}

Paste or save the job description here.

Source: [URL]
Date Found: {datetime.now().strftime('%Y-%m-%d')}
""",
        "communication-log.md": f"""# Communication Log - {company} {position}

Track all interactions with the company here.

## {datetime.now().strftime('%Y-%m-%d')} - Applied
- Submitted application via [source]
- Application link: [URL]

""",
        "notes.md": f"""# Notes - {company} {position}

## Company Research
-

## Position Details
-

## Key Points for Interview
-

## Questions to Ask
-
"""
    }

    for filename, content in files_to_create.items():
        file_path = folder_path / filename
        if not file_path.exists():
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"✓ Created {filename}")
        else:
            print(f"⚠ {filename} already exists, skipping")

    print(f"\n✅ Application folder created at: {folder_path}")
    return folder_path

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python create_application_folder.py <applications_dir> <company> <position>")
        print('Example: python create_application_folder.py ./applications "Google" "Senior Engineer"')
        sys.exit(1)

    applications_dir = sys.argv[1]
    company = sys.argv[2]
    position = sys.argv[3]

    create_application_folder(applications_dir, company, position)
