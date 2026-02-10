# Publishing Your Plugin - Complete Guide

## What You Have Now

A complete **plugin** structure that others can install with:

```bash
claude plugin install duncanapm/job-search-assistant-plugin
```

## Plugin vs Skill - Key Difference

**Plugin** (what you have now):
- Complete package with skills + config + documentation
- Installable via `claude plugin install`
- Shows up in plugin marketplaces
- Easier for users to discover and install

**Skill** (what we had before):
- Just the instructions
- Installed via `claude skill install`
- Less discoverable

## Step-by-Step Publishing

### 1. Create GitHub Repository

Go to https://github.com/new

- **Name**: `job-search-assistant-plugin`
- **Description**: "Complete job search workflow management plugin for Claude"
- **Visibility**: ✅ **Public** (required)
- **Add**: ✅ README file, ✅ .gitignore (Python), ✅ MIT License
- Click **Create repository**

### 2. Push Your Plugin

```bash
# Navigate to your plugin directory
cd /path/to/job-search-plugin-complete

# Initialize git
git init

# Add files
git add .

# Commit
git commit -m "Initial release: Job Search Assistant Plugin v1.0.0"

# Add remote (use YOUR GitHub URL)
git remote add origin https://github.com/duncanapm/job-search-assistant-plugin.git

# Rename branch to main
git branch -M main

# Push
git push -u origin main
```

### 3. Tag and Release

```bash
# Tag the version
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push the tag
git push origin v1.0.0
```

### 4. Create GitHub Release

On GitHub:
1. Go to your repository → **Releases** → **Create a new release**
2. **Choose tag**: v1.0.0
3. **Release title**: "Job Search Assistant Plugin v1.0.0"
4. **Description**:
   ```markdown
   ## 🎉 Initial Release

   Complete job search workflow management for Claude Code.

   ### Features
   - Multi-platform job search (Indeed, Dice)
   - Application tracking spreadsheet
   - Resume tailoring suggestions
   - Follow-up automation
   - Interview preparation

   ### Installation
   ```bash
   claude plugin install duncanapm/job-search-assistant-plugin
   ```
   ```
5. Click **Publish release**

## How Users Install Your Plugin

Once published, users can install it three ways:

### Option 1: GitHub Username/Repo (Simplest)
```bash
claude plugin install duncanapm/job-search-assistant-plugin
```

### Option 2: Full GitHub URL
```bash
claude plugin install https://github.com/duncanapm/job-search-assistant-plugin
```

### Option 3: Browse and Install
```bash
# List available plugins
claude plugin search job

# Install from list
claude plugin install job-search-assistant
```

## Register in Plugin Marketplace

### Check Official Marketplace

1. Visit https://docs.anthropic.com or Claude app
2. Look for "Plugin Marketplace" or "Plugin Registry"
3. If available, submit your plugin:
   - Repository URL
   - Description
   - Category: Productivity
   - Keywords: job-search, career, resume

### Community Registries

Search GitHub for:
- "awesome-claude-plugins"
- "claude-plugin-registry"
- "claude-marketplace"

Submit a PR to add your plugin to the list.

### Create marketplace.json (Optional)

If marketplaces require metadata:

```json
{
  "id": "duncanapm/job-search-assistant-plugin",
  "name": "Job Search Assistant",
  "description": "Complete job search workflow management",
  "author": "Duncan",
  "category": "productivity",
  "tags": ["job-search", "career", "resume"],
  "repository": "https://github.com/duncanapm/job-search-assistant-plugin",
  "install": "claude plugin install duncanapm/job-search-assistant-plugin"
}
```

## Promote Your Plugin

### GitHub Topics
Add these topics to your repository:
- `claude-code`
- `claude-plugin`
- `claude-cowork`
- `job-search`
- `career`
- `productivity`
- `resume`

### Social Media
- Post on Twitter/X: "Just released a Claude plugin for job searching! 🚀"
- Share in r/ClaudeAI on Reddit
- Post in Claude Discord/Slack communities

### Write About It
- Blog post: "How I Built a Job Search Plugin for Claude"
- Demo video on YouTube
- Tutorial on Medium

## Maintaining Your Plugin

### Version Updates

When releasing updates:

```bash
# Update version in plugin.json
# Update README.md changelog

git commit -am "Release v1.1.0: Add new features"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push && git push --tags

# Create new GitHub release
```

### Responding to Issues

- Monitor GitHub Issues
- Respond to user questions
- Fix bugs promptly
- Consider feature requests

### Community Building

- Accept PRs from contributors
- Update documentation based on feedback
- Share success stories
- Build a community around your plugin

## Testing Before Publishing

### Test Locally

```bash
# From your plugin directory
claude plugin install .

# Verify it works
claude plugin list

# Try it out
# Ask Claude: "Help me organize my job search"

# Uninstall when done testing
claude plugin uninstall job-search-assistant
```

### Test from GitHub

After pushing:

```bash
# Install from your repo
claude plugin install duncanapm/job-search-assistant-plugin

# Test all features
# Then uninstall and reinstall to test the install process
```

## Common Issues

### "Plugin not found"
- Make sure repository is public
- Check that plugin.json exists in root
- Verify repository name matches

### "Installation failed"
- Check plugin.json syntax (valid JSON)
- Ensure skills/ directory exists
- Verify file paths in plugin.json are correct

### "Plugin installed but not working"
- Check skill paths in plugin.json
- Verify SKILL.md exists
- Check Claude logs: `claude logs`

## Quick Checklist Before Publishing

- [ ] Repository is public on GitHub
- [ ] plugin.json in root with correct paths
- [ ] README.md with installation instructions
- [ ] LICENSE file (MIT recommended)
- [ ] skills/ directory with your skill
- [ ] Documentation in docs/
- [ ] Tagged version (v1.0.0)
- [ ] GitHub release created
- [ ] Tested installation works

## Next Steps

1. **Push to GitHub** using commands above
2. **Create release** with v1.0.0 tag
3. **Test installation**: `claude plugin install duncanapm/job-search-assistant-plugin`
4. **Share it** on social media and communities
5. **Submit to marketplaces** if they exist

---

**Your plugin is ready!** Follow these steps and others will be able to easily install and use it.

Questions? Open an issue or email duncanapm@gmail.com
