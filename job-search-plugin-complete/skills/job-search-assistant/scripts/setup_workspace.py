#!/usr/bin/env python3
"""
Helper script to set up the job search workspace structure.
"""
import os
import sys
import shutil
from pathlib import Path

def setup_workspace(base_path):
    """Create the standard job search folder structure."""
    base = Path(base_path)

    # Create main directories
    directories = [
        base / "base-materials",
        base / "applications",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created {directory.relative_to(base.parent)}")

    # Copy tracker template
    skill_path = Path(__file__).parent.parent
    template_path = skill_path / "assets" / "tracker-template.xlsx"

    if template_path.exists():
        tracker_path = base / "job-tracker.xlsx"
        shutil.copy(template_path, tracker_path)
        print(f"✓ Created job tracker at {tracker_path.relative_to(base.parent)}")
    else:
        print(f"⚠ Template not found at {template_path}")

    # Create README
    readme_path = base / "README.md"
    readme_content = """# Job Search Workspace

## Structure

- **job-tracker.xlsx** - Master spreadsheet tracking all applications
- **base-materials/** - Your master resume and cover letter templates
- **applications/** - One folder per company/position with tailored materials

## Workflow

1. Search for jobs using Indeed/Dice connectors
2. Add promising roles to job-tracker.xlsx
3. Create application folder for each job you're applying to
4. Tailor resume/cover letter based on suggestions
5. Track follow-ups and interview progress in the tracker

## Application Folder Structure

Each application folder should contain:
- job-description.txt (or .pdf)
- tailoring-suggestions.md (recommendations for customization)
- resume-tailored.docx (customized version)
- cover-letter.docx
- follow-up-draft-YYYY-MM-DD.txt (any follow-up emails)
- interview-prep.md (if you get to interview stage)
- communication-log.md (track all interactions)

## Tips

- Update the tracker immediately after any action
- Set "Next Action" dates to stay on top of follow-ups
- Keep job descriptions saved for reference during interviews
- Review tailoring suggestions before applying
"""

    with open(readme_path, 'w') as f:
        f.write(readme_content)
    print(f"✓ Created README at {readme_path.relative_to(base.parent)}")

    print(f"\n✅ Workspace setup complete at {base}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python setup_workspace.py <workspace_path>")
        sys.exit(1)

    workspace_path = sys.argv[1]
    setup_workspace(workspace_path)
