---
name: jobflow
description: Job search workflow - track applications, tailor resumes/CVs, automate follow-ups, prep interviews. Triggers on job hunting, resume, cv, applications.
---

# JobFlow - Job Search Assistant

## Overview

This skill helps you manage your entire job search workflow from discovery to offer. It integrates with job boards (Indeed, Dice), maintains a tracking spreadsheet, organizes materials per company, suggests resume/cover letter improvements, and automates follow-up reminders.

## Core Capabilities

This skill provides four integrated capabilities that work together:

### 1. Job Tracker (Spreadsheet Management)
Maintains a master spreadsheet (Numbers/Excel) with high-level status of your search:
- Company name, position, date applied, status (Applied, Phone Screen, Interview, Offer, Rejected)
- Application links, contact info, salary range
- Next action date and follow-up status
- Quick filtering and status summaries

### 2. Application Manager (Per-Company Folders)
Creates organized folders for each application containing:
- Job description saved as text/PDF
- Tailored resume version
- Cover letter
- Communication log
- Interview notes
- Any company research

### 3. Resume/CV Tailor (Suggestion Mode)
Analyzes job postings and suggests specific improvements to your resume/CV/cover letter:
- Keywords to add from job description
- Skills to emphasize
- Experience to highlight
- Sections to reorder
- **Does NOT automatically rewrite** - provides suggestions for you to implement

### 4. Follow-Up Assistant
Manages follow-up timing and drafts:
- Tracks days since last contact
- Suggests optimal follow-up timing (typically 5-7 days after application, 2-3 days after interview)
- Drafts follow-up emails for your review
- Creates reminders for next actions

## Quick Start Workflow

When a user says "help me with my job search", ask these essential questions to get started:

1. **What country are you job searching in?** (e.g., United States, United Kingdom, Canada, Australia - critical for filtering relevant jobs)
2. **What specific job title are you looking for to start?** (e.g., "Senior Software Engineer", "Product Manager", "Data Analyst" - you can add more role preferences later)
3. **Where should I create the tracking spreadsheet and application folders?** (suggest ~/Documents/job-search or similar dedicated location)

**That's it!** You can add additional preferences later:
- More job titles or role types
- Specific cities or remote-only filters
- Salary ranges
- Company size preferences
- Remote/hybrid/onsite requirements
- Your base resume/CV location

Then set up the structure:
```
job-search/
├── job-tracker.numbers (or .xlsx)
├── base-materials/
│   ├── resume-master.docx (or cv-master.docx)
│   └── cover-letter-template.docx
└── applications/
    ├── company-a-position/
    ├── company-b-position/
    └── ...
```

## Task-Based Workflows

### Finding Jobs

**User request patterns:**
- "Search for software engineer jobs in Seattle"
- "Find product manager roles at tech companies"
- "Look for remote data analyst positions"

**Process:**
1. **CRITICAL: Confirm user's country first** (if not already established during onboarding)
2. Use MCP connectors (Indeed, Dice) to search multiple platforms
3. Filter by user's preferred country/location, job title, and any additional preferences (salary, remote options, etc.)
4. Present top matches with: title, company, location, salary, posting date
5. Ask which jobs to track or apply to

### Tracking an Application

**User request patterns:**
- "Add this job to my tracker"
- "I just applied to Google"
- "Track this application"

**Process:**
1. Open/create the tracking spreadsheet
2. Add new row with: Company, Position, Date Applied, Status="Applied", Link
3. Create a corresponding folder in applications/
4. Save job description to the folder
5. Set follow-up reminder for 7 days out
6. Confirm tracking is set up

### Tailoring Resume/CV/Cover Letter

**User request patterns:**
- "Help me tailor my resume/CV for this job"
- "What should I change in my cover letter?"
- "Customize my application for this role"

**Process:**
1. Read the job description (from link, text, or saved file)
2. Read user's base resume/CV
3. Analyze the gap: required skills, keywords, experience emphasis
4. **Provide suggestions in a markdown file** saved to the application folder:
   - "Add keyword 'Kubernetes' to Technical Skills section"
   - "Emphasize team leadership experience in Role X"
   - "Reorder projects to put Y project first (matches their tech stack)"
   - "Include metric about Z accomplishment (they mention scale)"
5. Ask if user wants to make changes or if they'd like you to create a draft
6. If they want a draft, create tailored-resume.docx (or tailored-cv.docx) in the application folder

**Critical: Never automatically replace their resume/CV** - always provide suggestions first and get approval.

### Following Up

**User request patterns:**
- "What applications need follow-up?"
- "Draft a follow-up email for Company X"
- "It's been a week since I applied, should I reach out?"

**Process:**
1. Check tracking spreadsheet for applications where:
   - Status="Applied" and >7 days since application
   - Status="Phone Screen" and >3 days since interview
   - Status="Interview" and >2 days since final interview
2. List applications needing follow-up
3. For each selected:
   - Draft a polite, brief follow-up email
   - Save to application folder as follow-up-draft-[date].txt
   - Update tracking spreadsheet with "Follow-up Sent" and new date
4. Present drafts for user review before any actual sending

### Interview Preparation

**User request patterns:**
- "Help me prep for my interview at Company X"
- "Research this company for my interview"
- "What questions should I prepare?"

**Process:**
1. Create interview-prep.md in the application folder
2. Research company (web search if needed):
   - Recent news, products, culture
   - Common interview questions for the role
   - Questions to ask the interviewer
3. Review job description to identify key topics
4. Suggest talking points based on user's experience
5. Create a checklist of prep tasks

## Integration with MCP Connectors

This skill works with these connectors (suggest connecting if not already available):

**Indeed** - Search jobs, get job details
**Dice** - Tech job search
**Gmail** (optional) - Send follow-up emails, track responses
**Google Drive** (optional) - Store materials in cloud
**Calendar** (optional) - Schedule interview prep time

When connectors aren't available, fall back to manual processes (user provides job listings, we organize and track).

## Spreadsheet Schema

The job-tracker spreadsheet should have these columns:

| Column | Description | Example |
|--------|-------------|---------|
| Company | Company name | Google |
| Position | Job title | Senior Software Engineer |
| Date Applied | When you applied | 2026-02-01 |
| Status | Current stage | Phone Screen |
| Link | Job posting URL | https://... |
| Contact | Recruiter/contact info | jane@google.com |
| Salary Range | If provided | $150k-200k |
| Next Action | What's next | Follow up by 2/15 |
| Notes | Quick notes | Referral from John |

Use conditional formatting to color-code statuses:
- Applied = Blue
- Phone Screen = Yellow
- Interview = Orange
- Offer = Green
- Rejected = Gray

## Example Interactions

**Example 1: Starting a job search**
```
User: I need to organize my job search
Claude: I'll help you set up a complete job search system. Just need 3 quick things:
1. What country are you job searching in?
2. What specific job title are you looking for to start? (e.g., "Senior Software Engineer")
3. Where should I create your tracking spreadsheet and application folders?

User: United States, Senior Product Manager, ~/Documents/job-search
Claude: Perfect! I'll create:
- A tracking spreadsheet at ~/Documents/job-search/job-tracker.xlsx
- An applications folder to organize materials per company
- A base-materials folder for your resume/CV templates

I'll focus searches on Senior Product Manager roles in the United States. Ready to start searching?

(You can add more preferences like specific cities, salary range, or additional role titles anytime by just asking!)
```

**Example 2: Tailoring a resume/CV**
```
User: Help me tailor my CV for this Product Manager job at Meta
Claude: [Reads job description and base CV]

I've created tailoring-suggestions.md in your applications/meta-pm folder. Here are the key changes I recommend:

**High Priority:**
1. Add "A/B testing" and "experimentation" keywords (mentioned 3x in job description)
2. Move your Instagram growth project to the top - it directly matches their social media focus
3. Quantify the impact in your current PM role (they emphasize metrics-driven decision making)

**Medium Priority:**
4. Emphasize cross-functional collaboration (mentioned in 2 bullet points)
5. Add SQL to your technical skills if you have experience

Would you like me to create a draft tailored CV with these changes, or will you make the edits yourself?
```

**Example 3: Follow-up check**
```
User: What needs follow-up?
Claude: [Checks spreadsheet]

Three applications need follow-up:

1. **Stripe - Senior Engineer** (Applied 9 days ago)
   - Suggested action: Send follow-up email

2. **Airbnb - Tech Lead** (Phone screen 4 days ago)
   - Suggested action: Thank you + timeline check

3. **Netflix - Principal Engineer** (Final interview 3 days ago)
   - Suggested action: Brief check-in on decision timeline

I've drafted follow-up emails for each in their application folders. Would you like to review and send them?
```

## Best Practices

**Organization:**
- Keep one master tracking spreadsheet (don't split by status)
- Use consistent folder naming: `company-name-position-title`
- Date all follow-up drafts: `follow-up-2026-02-15.txt`

**Resume/CV Tailoring:**
- Always provide suggestions before making changes
- Keep the original resume/CV structure unless user requests major restructuring
- Focus on keyword optimization and emphasis, not complete rewrites

**Follow-up Timing:**
- 5-7 days after application
- 2-3 days after phone screen
- 2 days after final interview
- Never more than 2 follow-ups without response

**Tracking:**
- Update spreadsheet immediately after any action
- Log all communications in the application folder
- Set clear "Next Action" dates

## Resources

### scripts/
Contains utility scripts for spreadsheet operations and folder management. These are executed as needed and generally don't need to be loaded into context.

### references/
Contains detailed guides that Claude should reference:
- `resume-tailoring-guide.md` - Detailed instructions on analyzing job descriptions and making suggestions
- `follow-up-templates.md` - Template library for various follow-up scenarios

### assets/
Contains template files:
- `tracker-template.xlsx` - Pre-formatted tracking spreadsheet
- `application-folder-template/` - Folder structure template
