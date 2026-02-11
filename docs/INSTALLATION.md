# Job Search Assistant Plugin - Installation Guide

## What This Plugin Does

The Job Search Assistant helps you manage your entire job search workflow:

- 🔍 **Multi-platform job search** - Search Indeed, Dice, and other job boards
- 📊 **Application tracking** - Spreadsheet tracker with status, follow-ups, and statistics
- 📁 **Organization** - Per-company folders with job descriptions, notes, and communications
- ✍️ **Resume tailoring** - Get specific suggestions for customizing your resume per job
- 📧 **Follow-up automation** - Timed reminders and pre-drafted follow-up emails
- 💼 **Interview prep** - Company research and preparation materials

## Installation

### Option 1: Quick Install (Recommended)

If you have Claude Code CLI installed:

```bash
claude skill install job-search-assistant.skill
```

### Option 2: Manual Install

1. Extract the `.skill` file (it's a tar.gz archive):
   ```bash
   tar -xzf job-search-assistant.skill -C ~/.claude/skills/
   ```

2. Restart Claude or reload skills:
   ```bash
   claude reload
   ```

## Setup

### 1. Connect Job Board Services (Optional but Recommended)

To search jobs directly from Claude, connect these services:

- **Indeed** - Search millions of jobs
- **Dice** - Tech-focused job board

When you ask Claude to search for jobs, it will suggest connecting these if they're not already available.

### 2. First-Time Use

When you first use the plugin, Claude will:

1. Ask where you want to set up your job search workspace
2. Create a folder structure:
   ```
   job-search/
   ├── job-tracker.xlsx          # Master tracking spreadsheet
   ├── base-materials/           # Your resume and cover letter templates
   └── applications/             # Per-company folders
   ```
3. Copy a pre-formatted tracking spreadsheet

## How to Use

### Starting Your Job Search

```
You: Help me organize my job search for product manager roles
```

Claude will set up your workspace and guide you through the process.

### Searching for Jobs

```
You: Search for senior software engineer jobs in Seattle
```

Claude will search across job boards and present top matches.

### Tracking an Application

```
You: Add this Google job to my tracker
[paste job link or details]
```

Claude will:
- Add it to your tracking spreadsheet
- Create an application folder
- Save the job description
- Set a follow-up reminder

### Tailoring Your Resume

```
You: Help me tailor my resume for this Meta role
```

Claude will:
- Analyze the job description
- Compare it to your base resume
- Provide specific suggestions (not automatic changes!)
- Create a suggestions file in the application folder
- Optionally create a tailored draft if you request it

### Following Up

```
You: What applications need follow-up?
```

Claude will:
- Check your tracking spreadsheet
- List applications that need attention
- Draft follow-up emails for your review
- Update the tracker after you send them

### Interview Prep

```
You: Help me prep for my interview at Stripe
```

Claude will:
- Research the company
- Suggest common interview questions
- Create a prep document
- Help you prepare talking points

## Features

### Tracking Spreadsheet

The job-tracker.xlsx includes:
- **Job Tracker** sheet - Main tracking with color-coded statuses
- **Statistics** sheet - Automatic metrics (response rate, applications by status, etc.)
- **Instructions** sheet - Quick reference guide

### Resume Tailoring Suggestions

Claude analyzes job descriptions and provides:
- Missing keywords to add
- Skills to emphasize
- Experience to highlight
- Sections to reorder
- Specific phrasing suggestions

**Important:** Claude suggests changes but doesn't automatically rewrite your resume. You review suggestions and decide what to implement.

### Follow-Up Templates

Pre-written templates for:
- Post-application follow-up (5-7 days)
- Post-phone screen thank you (24 hours)
- Post-interview thank you (24 hours)
- Timeline check-ins (2-3 days)
- Second follow-up (if no response)
- Post-rejection relationship building

### Application Folders

Each application folder contains:
- job-description.txt
- tailoring-suggestions.md
- resume-tailored.docx (if created)
- cover-letter.docx
- follow-up-draft-YYYY-MM-DD.txt
- interview-prep.md
- communication-log.md
- notes.md

## Example Workflows

### Workflow 1: Finding and Applying to a Job

1. **Search**: "Search for data analyst jobs in Austin"
2. **Review**: Claude presents top matches
3. **Track**: "Add the Indeed job at Dell to my tracker"
4. **Tailor**: "Help me tailor my resume for this Dell role"
5. **Review Suggestions**: Read the tailoring-suggestions.md file
6. **Apply**: Make changes and apply through the job board
7. **Follow-up**: After 7 days, "What needs follow-up?"

### Workflow 2: Managing Multiple Applications

1. **Check Status**: "Show me all my active applications"
2. **Follow-up Check**: "What applications need follow-up?"
3. **Draft Emails**: Claude creates follow-up drafts for each
4. **Review and Send**: You review, edit, and send the emails
5. **Update Tracker**: Claude updates your spreadsheet

### Workflow 3: Interview Preparation

1. **Request Prep**: "Help me prep for my Google interview next week"
2. **Research**: Claude researches the company and role
3. **Questions**: Suggests common questions for the role
4. **Talking Points**: Reviews your experience for relevant examples
5. **Checklist**: Creates a prep checklist

## Tips for Success

### Organization
- Update the tracker immediately after any action
- Keep job descriptions saved (you'll reference them in interviews)
- Use consistent naming: `company-name-position-title`
- Date all follow-up drafts

### Resume Tailoring
- Always review suggestions before making changes
- Focus on keyword optimization, not complete rewrites
- Keep your original resume structure unless you want major changes
- Tailor for each application (yes, it takes time, but it works!)

### Follow-Up Timing
- 5-7 days after application
- 2-3 days after phone screen
- 2 days after interview
- Never more than 2 follow-ups without response

### Tracking
- Set "Next Action" dates for everything
- Log all communications in application folders
- Review your statistics weekly to adjust strategy

## Troubleshooting

### "Claude isn't using the skill"

Make sure you're using phrases that trigger it:
- "Help me with my job search"
- "Search for [role] jobs"
- "Track this application"
- "Tailor my resume"
- "What needs follow-up?"

### "I don't have Indeed/Dice connectors"

The skill works without them! You can:
- Search manually and give Claude the job listings
- Copy/paste job descriptions
- Let Claude organize and track everything else

### "Claude rewrote my entire resume"

This shouldn't happen! The skill instructs Claude to provide suggestions, not automatic rewrites. If it happens, say: "Please just give me suggestions, don't rewrite it."

### "The tracking spreadsheet isn't calculating"

The formulas should auto-calculate. If not:
- Make sure you're saving the file
- Try opening it in Excel or LibreOffice
- Check that you have data in the tracker (formulas need data)

## Support

This plugin was created with Claude Code's skill-creator. To:
- Report issues
- Request features
- Suggest improvements

Open an issue or submit a PR on the repository (if public), or provide feedback directly to the plugin creator.

## Version

Version: 1.0.0
Created: February 2026
Compatible with: Claude Code / Cowork mode

---

Good luck with your job search! 🚀
