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

When a user starts, ask only **two questions**:

1. **What country are you in?** (e.g., UK, US, Canada, Australia)
2. **Give me one job title to start with.** (e.g., "Senior Sales Engineer", "Product Manager")

**That's it.** Do NOT ask about folders, spreadsheets, resume locations, or preferences upfront. Get straight to results.

### Immediate Next Step: Show 5 Matching Jobs with Quick Triage

As soon as you have country + job title, immediately search and present **5 matching jobs** with a quick-triage prompt so the user can rapidly sort them:

```
Here are 5 Senior Sales Engineer roles in the UK:

1. **Datadog** — Senior Sales Engineer, London (£90-120k)
2. **Splunk** — Senior Sales Engineer, Remote UK (£85-110k)
3. **New Relic** — Senior SE, Manchester (£80-105k)
4. **Dynatrace** — Sales Engineer, London (£95-125k)
5. **Elastic** — Senior Sales Engineer, Remote UK (£88-115k)

Quick triage — for each, tell me:
  ✅ Interested    ❌ Pass    📋 Apply now

e.g. "1 ✅, 2 ❌, 3 ✅, 4 ❌, 5 📋" or just "1,3 interested, 5 apply, rest pass"
```

**How triage responses work:**
- **✅ Interested** — Save to a shortlist for later. No tracking folder yet.
- **❌ Pass** — Skip it, don't show again. Note the reason if given (helps refine future results).
- **📋 Apply now** — Immediately set up tracking: create application folder, save job description, and begin the application workflow (resume tailoring, cover letter, etc.)

The user can respond in any format — numbers, emojis, words, or a mix. Be flexible in parsing. Examples:
- "1 and 3 look good, pass on the rest, apply to 5"
- "1✅ 2❌ 3✅ 4❌ 5📋"
- "interested in Datadog and New Relic, apply to Elastic, skip the others"

After triage, summarize what happened:
```
Got it:
  ✅ Shortlisted: Datadog, New Relic
  📋 Applying: Elastic — setting up your application now
  ❌ Passed: Splunk (noted), Dynatrace (noted)

Want me to search for more, or start on your Elastic application?
```

### Then Refine Through Conversation

After showing initial results, let the user naturally narrow down. They might say things like:
- "Focus on AI Observability companies"
- "Only pre-IPO companies"
- "Remote only"
- "£100k+ base"
- "Series C or later"
- "Show me more like Datadog and New Relic"

Each time they refine, search again and show updated results with the same triage prompt. Build up their preferences organically through this back-and-forth rather than asking everything upfront.

Use pass reasons to improve results. If user passes on 3 jobs and says "too big / too corporate", factor that into future searches automatically.

### When to Set Up Tracking

Only create the folder structure and spreadsheet when the user **applies** to a job (📋 Apply now). At that point, automatically create `~/job-search` (or ask if first time) and set up:
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

**Shortlisted jobs** (✅) are tracked in a lightweight list (in the spreadsheet or in memory) — no folder until the user decides to apply.

## Task-Based Workflows

### Finding Jobs

**User request patterns:**
- "Search for software engineer jobs in Seattle"
- "Find product manager roles at tech companies"
- "Look for remote data analyst positions"
- "Show me AI Observability companies"
- "Only pre-IPO startups"

**Process:**
1. Use MCP connectors (Indeed, Dice) or web search to find matching roles
2. Apply all accumulated filters (country, title, plus any refinements like market segment, company stage, remote preference)
3. Present **5 results** with: company, title, location, salary range
4. Wait for user to refine further or act on specific listings
5. Each refinement round updates results — don't re-ask questions already answered

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
User: I need help with my job search
Claude: Two quick questions to get started:
1. What country are you in?
2. Give me one job title to start with.

User: UK, Senior Sales Engineer
Claude: Here are 5 Senior Sales Engineer roles in the UK:

1. **Datadog** — Senior Sales Engineer, London (£90-120k)
2. **Splunk** — Senior Sales Engineer, Remote UK (£85-110k)
3. **New Relic** — Senior SE, Manchester (£80-105k)
4. **Dynatrace** — Sales Engineer, London (£95-125k)
5. **Elastic** — Senior Sales Engineer, Remote UK (£88-115k)

Quick triage — for each, tell me:
  ✅ Interested    ❌ Pass    📋 Apply now
e.g. "1,3 interested, 5 apply, rest pass"

User: 1 and 3 interested, rest pass — too enterprise. Focus on AI Observability, pre-IPO
Claude: Got it:
  ✅ Shortlisted: Datadog, New Relic
  ❌ Passed: Splunk, Dynatrace, Elastic (too enterprise — noted, filtering smaller companies)

Here are 5 Senior Sales Engineer roles at pre-IPO AI Observability companies in the UK:

1. **Arize AI** — Senior Sales Engineer, Remote UK (£95-125k) — Series C
2. **Weights & Biases** — Senior SE, London (£90-120k) — Series C
3. **Comet ML** — Sales Engineer, Remote UK (£85-110k) — Series B
4. **Helicone** — Senior Sales Engineer, London (£100-130k) — Series A
5. **Langfuse** — Sales Engineer, Remote UK (£80-105k) — Series A

  ✅ Interested    ❌ Pass    📋 Apply now

User: 1 and 2 apply, 3 interested, pass on 4 and 5 — too early stage
Claude: Got it:
  📋 Applying: Arize AI, Weights & Biases — setting up applications now
  ✅ Shortlisted: Comet ML (added to your list with Datadog & New Relic)
  ❌ Passed: Helicone, Langfuse (too early stage — noted, Series B+ from now on)

Creating your job search workspace at ~/job-search...
[Sets up folders, tracker, application folders for Arize AI and W&B]

Your Arize AI and W&B application folders are ready. Want to start tailoring your CV for one of these?
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
