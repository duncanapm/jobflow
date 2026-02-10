# Resume Tailoring Guide

This guide provides detailed instructions for analyzing job descriptions and creating tailoring suggestions for users' resumes and cover letters.

## Philosophy

The goal is to help users optimize their existing materials for specific roles, NOT to rewrite their resume from scratch. We provide specific, actionable suggestions that users can implement themselves, or optionally create a tailored draft if they request it.

## Analysis Process

### Step 1: Parse the Job Description

Extract these key elements:

1. **Required Skills** - Technical skills, tools, frameworks explicitly mentioned
2. **Preferred Skills** - "Nice to have" qualifications
3. **Soft Skills** - Communication, leadership, teamwork mentions
4. **Experience Level** - Years required, seniority indicators
5. **Responsibilities** - Day-to-day tasks and expectations
6. **Keywords** - Repeated terms that likely matter for ATS (Applicant Tracking Systems)
7. **Company Values** - Mission, culture indicators
8. **Metrics/Scale** - Team size, user numbers, data volume mentions

### Step 2: Analyze User's Resume

Map out their existing content:

1. **Skills Section** - What technical/soft skills are listed
2. **Experience** - Roles, companies, responsibilities, achievements
3. **Projects** - Side projects, major accomplishments
4. **Education** - Degrees, certifications
5. **Keywords Present** - What job-relevant terms already appear
6. **Quantifiable Achievements** - Metrics, percentages, growth numbers

### Step 3: Gap Analysis

Compare job requirements to resume content:

**Missing Keywords:**
- Required skills not mentioned at all
- Synonyms used instead of exact terms (e.g., "React" vs "React.js")
- Industry jargon they use that user doesn't

**Underemphasized Content:**
- Relevant experience buried in later bullets
- Projects that match their stack mentioned briefly
- Achievements that align with their metrics

**Overemphasized Content:**
- Skills/experience that don't match this role
- Content taking up space when not relevant

## Suggestion Framework

Organize suggestions by priority and specificity.

### High Priority Suggestions

These have the most impact on ATS and human reviewers:

**Add Missing Keywords:**
```
Add "[exact keyword]" to your [section name]:
- Where: [Specific location in resume]
- Why: Job description mentions this [X times/in requirements]
- How: [Specific phrasing suggestion if relevant]
```

**Emphasize Relevant Experience:**
```
Move [specific bullet/project] higher in [section]:
- Currently: [Current position]
- Suggested: [New position]
- Why: Directly matches their focus on [specific requirement]
```

**Add Quantifiable Metrics:**
```
Quantify the impact of [specific accomplishment]:
- Current: "[current phrasing]"
- Suggested: Add metric about [scale/growth/improvement]
- Why: Job description emphasizes [metrics-driven decision making/scale/growth]
```

### Medium Priority Suggestions

These improve alignment but are less critical:

**Reframe Experience:**
```
Reframe [experience] to emphasize [aspect]:
- Why: Job description mentions [specific requirement]
- Current focus: [what's currently emphasized]
- Suggested focus: [what should be emphasized]
```

**Add Related Skills:**
```
If you have experience with [skill], add it to [section]:
- Why: Commonly used with [required skill they mention]
- Priority: Medium (not explicitly required but relevant)
```

### Low Priority Suggestions

Nice-to-have improvements:

**Terminology Alignment:**
```
Use their terminology "[their term]" instead of "[your term]":
- Why: Matches company's language/industry standards
- Impact: Minor but shows attention to detail
```

## Output Format

Create a markdown file named `tailoring-suggestions.md` in the application folder:

```markdown
# Resume Tailoring Suggestions for [Company] - [Position]

Analysis Date: [Date]
Job Description: [Link or "Saved in job-description.txt"]

## Summary

[2-3 sentence overview of main alignment and gaps]

## High Priority Changes

### 1. [Suggestion Title]
**Action:** [Specific action to take]
**Location:** [Where in resume]
**Reason:** [Why this matters for this job]
**Details:** [Any specific phrasing or context]

### 2. [Next suggestion]
...

## Medium Priority Changes

[Same format as above]

## Low Priority Changes

[Same format as above]

## Keywords to Incorporate

The following keywords appear in the job description but not in your resume:
- [keyword 1] - [context where it appears]
- [keyword 2] - [context where it appears]

Consider adding these naturally where relevant.

## Overall Alignment: [X%]

Based on:
- Required skills match: [X/Y]
- Experience level match: [Assessment]
- Keyword coverage: [X%]

## Next Steps

1. Review these suggestions and decide which to implement
2. Let me know if you'd like me to create a tailored draft resume
3. After updating, we can review the cover letter

---

*These are suggestions to optimize your resume for this specific role. Your experience and skills remain the foundation - we're just highlighting the most relevant aspects for this opportunity.*
```

## Cover Letter Tailoring

Apply similar analysis to cover letters:

**Paragraph 1 (Hook):**
- Mention specific company achievements/products that align with user's interests
- Reference relevant skills from user's background

**Paragraph 2-3 (Body):**
- Highlight 2-3 specific experiences that match key job requirements
- Use keywords and metrics from job description
- Show understanding of role challenges

**Paragraph 4 (Close):**
- Enthusiastic but professional
- Mention next steps / availability

## Special Cases

### Career Transition
If user is transitioning fields:
- Emphasize transferable skills
- Reframe experience in new field's terminology
- Focus on learning aptitude and recent relevant projects

### Over-Qualified
If user has more experience than required:
- Emphasize leadership and mentorship
- Focus on strategic thinking, not just execution
- Address potential concerns about overqualification

### Under-Experienced
If user is reaching for next level:
- Emphasize growth trajectory and fast learning
- Highlight any leadership/ownership in current role
- Showcase relevant side projects or learning

## Red Flags to Avoid

Never suggest:
- Lying or misrepresenting experience
- Adding skills user doesn't have
- Fabricating metrics or achievements
- Removing recent experience to hide career gaps
- Changing graduation dates or tenure

Always suggest:
- Honest reframing of existing experience
- Emphasizing genuinely relevant aspects
- Adding context to make achievements clearer
- Using stronger action verbs for real accomplishments

## Examples

### Example 1: Adding Missing Keywords

**Job Description mentions:** "Experience with Kubernetes, Docker, and container orchestration"

**User's Resume says:** "Deployed applications using containerization"

**Suggestion:**
```
### Add Specific Container Technology Keywords

**Action:** Update your Technical Skills section and deployment bullet point
**Location:**
- Technical Skills: Add "Kubernetes, Docker"
- Current Role, Bullet 3

**Current phrasing:**
"Deployed applications using containerization"

**Suggested phrasing:**
"Deployed applications using Docker containers orchestrated with Kubernetes, managing 20+ microservices"

**Reason:** Job description explicitly requires Kubernetes experience and mentions it 4 times. Using exact terminology improves ATS matching and shows you use industry-standard tools.
```

### Example 2: Reordering for Relevance

**Job Description emphasizes:** "Building data pipelines at scale"

**User's Resume:** Has a relevant data pipeline project in position 4 of 6 projects

**Suggestion:**
```
### Prioritize Data Pipeline Project

**Action:** Move "Real-time Analytics Pipeline" project to first position
**Location:** Projects section

**Why:** This job is specifically about building data pipelines processing millions of events. Your pipeline project directly demonstrates this capability, but it's currently 4th in your projects list. Moving it to the top ensures recruiters and ATS systems see your most relevant experience first.

**Additional:** Consider adding the metric about throughput if you tracked it ("Processed X events/second" or "Handled Y million daily events")
```

## Testing Suggestions

Before presenting suggestions to user, verify:
1. ✓ Are suggestions specific and actionable?
2. ✓ Did you provide exact locations in the resume?
3. ✓ Did you explain WHY each change matters?
4. ✓ Are all suggestions honest (no fabrication)?
5. ✓ Did you prioritize by impact?
6. ✓ Is the overall assessment realistic?

## After User Reviews

Once user reviews suggestions:
- If they want to make changes themselves: Offer to review the updated version
- If they want a draft: Create `resume-tailored-[company].docx` with changes applied
- If they disagree with suggestions: Adjust based on their feedback and domain knowledge
