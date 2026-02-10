# JobFlow

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/duncanapm/jobflow/releases)

Complete job search workflow management plugin for Claude Code and Cowork mode.

## ✨ Features

- 🔍 **Multi-platform Job Search** - Search Indeed, Dice, and other job boards
- 📊 **Application Tracking** - Pre-formatted spreadsheet with statistics
- 📁 **Organized Folders** - Per-company folders with all materials
- ✍️ **Resume Tailoring** - Specific suggestions (not auto-rewrites)
- 📧 **Follow-up Automation** - Timed reminders and email templates
- 💼 **Interview Prep** - Company research and preparation materials

## 🚀 Quick Install

```bash
claude plugin install duncanapm/jobflow
```

Or install from GitHub:

```bash
claude plugin install https://github.com/duncanapm/jobflow
```

## 📖 Quick Start

After installation, simply ask Claude:

```
Help me organize my job search for software engineer roles
```

Claude will:
1. Create a tracking spreadsheet
2. Set up folder structure
3. Guide you through the workflow

## 🎯 Common Commands

**Search for jobs:**
```
Search for product manager jobs in San Francisco
```

**Track an application:**
```
Add this Google job to my tracker
[paste job link]
```

**Tailor your resume:**
```
Help me tailor my resume for this Meta role
```

**Check follow-ups:**
```
What applications need follow-up?
```

**Prep for interviews:**
```
Help me prep for my interview at Stripe tomorrow
```

## 📂 What Gets Created

```
job-search/
├── job-tracker.xlsx              # Master spreadsheet
│   ├── Job Tracker (color-coded statuses)
│   ├── Statistics (auto-calculated)
│   └── Instructions
├── base-materials/               # Your templates
│   ├── resume-master.docx
│   └── cover-letter-template.docx
└── applications/                 # Per-company folders
    ├── google-senior-engineer/
    │   ├── job-description.txt
    │   ├── tailoring-suggestions.md
    │   ├── resume-tailored.docx
    │   ├── cover-letter.docx
    │   ├── follow-up-draft-2026-02-15.txt
    │   ├── interview-prep.md
    │   └── communication-log.md
    └── meta-product-manager/
        └── ...
```

## 🔌 Optional Integrations

The plugin works standalone, but integrates with:

- **Indeed** - Job search connector
- **Dice** - Tech job search connector
- **Gmail** - Email follow-ups (optional)
- **Google Drive** - Cloud storage (optional)
- **Calendar** - Interview scheduling (optional)

Claude will suggest connecting these when relevant.

## 💡 How It Works

### 1. Job Tracking
- Color-coded spreadsheet (Applied → Phone Screen → Interview → Offer)
- Automatic statistics (response rates, status breakdown)
- Next action reminders

### 2. Resume Tailoring (Suggestion-Based)
- Analyzes job descriptions
- Provides **specific suggestions** (not auto-rewrites)
- You stay in control of changes
- Creates tailoring-suggestions.md file

### 3. Follow-Up Management
- Pre-written templates for various scenarios
- Proper timing (5-7 days post-application, etc.)
- Draft emails for your review

### 4. Interview Preparation
- Company research
- Common interview questions
- Talking points from your experience

## 📋 Requirements

- Claude Code CLI or Cowork mode
- No external dependencies (MCP connectors are optional)

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md)

### Report Issues

Found a bug? [Open an issue](https://github.com/duncanapm/jobflow/issues)

### Request Features

Have ideas? [Start a discussion](https://github.com/duncanapm/jobflow/discussions)

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- Built with Claude Code's skill-creator
- Designed for job seekers who want to stay organized
- Inspired by modern job search challenges

## 📞 Support

- **GitHub Issues**: [Report bugs](https://github.com/duncanapm/jobflow/issues)
- **Discussions**: [Ask questions](https://github.com/duncanapm/jobflow/discussions)
- **Email**: duncanapm@gmail.com

## 🔄 Changelog

### v1.0.0 (2026-02-10)
- Initial release
- Multi-platform job search
- Application tracking spreadsheet
- Resume tailoring suggestions
- Follow-up automation
- Interview preparation

---

**Made with ❤️ for job seekers everywhere**

If this plugin helps you land your dream job, consider giving it a star! ⭐
