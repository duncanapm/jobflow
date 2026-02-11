# JobFlow Project Administration Guide

This guide explains how to manage the JobFlow project using Claude Code UI.

## 📁 Directory Structure

```
jobflow/
├── .git/                          # Git repository
├── .gitignore                     # Files to ignore in git
├── LICENSE                        # MIT license
├── README.md                      # Main documentation
├── PLUGIN-PUBLISHING.md           # Publishing guide
├── PROJECT-GUIDE.md              # This file
├── plugin.json                    # Plugin metadata
├── docs/                          # Documentation
│   └── INSTALLATION.md
├── mcps/                          # Optional MCP connectors
├── skills/                        # Skill files
│   └── jobflow/
│       ├── SKILL.md              # Main skill instructions
│       ├── assets/               # Templates (spreadsheets, etc.)
│       ├── references/           # Guides and templates
│       └── scripts/              # Helper scripts
```

## 🔧 Using Claude Code UI for Project Management

### File Explorer
- **Location**: Left sidebar in Claude desktop app
- **View files**: Click folders to expand
- **Edit files**: Click any file to open in editor
- **Create files**: Right-click folder → "New File"
- **Delete files**: Right-click → "Delete"

### Git Integration
The repository is now properly configured with:
- ✅ Git initialized
- ✅ Connected to https://github.com/duncanapm/jobflow.git
- ✅ Main branch created
- ✅ Initial commit made

**Common Git operations via Claude:**

```
# Check status
"Show me the git status"

# Commit changes
"Commit these changes with message: [your message]"

# Push to GitHub
"Push to GitHub"

# Create a new release
"Create a new release v1.0.1 with these changes..."
```

### Editing Files

**To update the skill:**
1. Ask Claude: "Open SKILL.md"
2. Claude will show you the file
3. Tell Claude what to change: "Add a section about X"
4. Claude will make the edit
5. Commit: "Commit this change"

**To update documentation:**
1. "Open README.md"
2. "Update the installation instructions to mention X"
3. "Commit the change"

### Building Distribution Files

**To create jobflow.zip for distribution:**

```bash
# Claude can run this for you
cd /sessions/fervent-sleepy-hamilton/jobflow
zip -r jobflow.zip skills/jobflow/
```

Then copy to outputs:
```bash
cp jobflow.zip /sessions/fervent-sleepy-hamilton/mnt/outputs/
```

**For GitHub releases:**
1. "Create jobflow.zip from the skills directory"
2. "Copy it to the outputs folder"
3. You manually upload to GitHub Releases

## 📝 Common Tasks

### Adding a New Feature to the Skill

**Method 1: Direct editing**
```
You: "Add a new section to SKILL.md about salary negotiation"
Claude: [edits the file]
You: "Commit this"
```

**Method 2: Via skill-creator**
```
You: "I want to improve the jobflow skill to include salary negotiation guidance"
Claude: [uses skill-creator to update]
```

### Updating Plugin Metadata

```
You: "Update plugin.json to version 1.1.0"
Claude: [edits plugin.json]
You: "Commit and create a GitHub release"
```

### Testing Changes Locally

1. Make your changes to SKILL.md
2. Rebuild the ZIP: "Create jobflow.zip"
3. Reinstall in Cowork:
   - Settings → Capabilities → Upload Skill
   - Select new jobflow.zip
   - Toggle off/on to reload

### Publishing a New Version

1. Make your changes
2. Update version in plugin.json
3. Update CHANGELOG in README.md
4. Commit changes: "Commit version 1.1.0"
5. Create ZIP: "Build jobflow.zip"
6. Upload to GitHub Releases manually
7. Users can download the new version

## 🔄 Git Workflow

### Before Making Changes
```
You: "Pull latest from GitHub"
Claude: [runs git pull]
```

### After Making Changes
```
You: "Show me what changed"
Claude: [shows git diff]

You: "Commit with message: Add salary negotiation feature"
Claude: [commits]

You: "Push to GitHub"
Claude: [pushes]
```

### Creating Branches
```
You: "Create a new branch called feature-salary-negotiation"
Claude: [creates branch]

You: [make changes]

You: "Commit and push this branch"
Claude: [commits and pushes]

You: "Create a pull request"
Claude: [creates PR via gh CLI]
```

## 🎯 Best Practices

### File Organization
- Keep SKILL.md as the main skill instructions
- Put templates in `skills/jobflow/assets/`
- Put reference docs in `skills/jobflow/references/`
- Put helper scripts in `skills/jobflow/scripts/`

### Version Control
- Commit frequently with clear messages
- Push to GitHub after each logical unit of work
- Use semantic versioning (1.0.0 → 1.1.0 → 2.0.0)

### Testing
- Test locally before publishing
- Keep a test installation in Cowork
- Ask Claude to "test the jobflow skill with [scenario]"

### Documentation
- Update README.md when features change
- Keep INSTALLATION.md current
- Update CHANGELOG with each version

## 🚀 Quick Commands

**View project:**
```
Show me the project structure
What files are in the jobflow directory?
```

**Edit files:**
```
Open SKILL.md
Update README.md to say X
Add Y to the references folder
```

**Git operations:**
```
Git status
Commit with message: [message]
Push to GitHub
Show me the diff
```

**Build and test:**
```
Create jobflow.zip
Test the jobflow skill
What happens if I ask Claude to [scenario]?
```

## 📞 Getting Help

- Ask Claude: "How do I [task] in this project?"
- Claude has full access to the project structure
- Claude can run git commands, edit files, and test changes

## 🔐 Security Notes

- Never commit sensitive data
- .gitignore prevents accidental commits of build files
- GitHub token/credentials never go in the repo

---

**You're all set!** The project is clean, organized, and ready for easy management through Claude Code UI.
