
# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
**GitLab AI Hackathon – Structured Setup Data**

---

### 1️⃣ Mandatory Requirements (Must‑Builds)

| # | Requirement | Details / Why it’s mandatory |
|---|-------------|------------------------------|
| 1 | **Create at least one *custom public agent* or *public flow*** | Must be built on the **GitLab Duo Agent Platform**; agents must react to triggers and take action (chat‑only bots are disqualified). |
| 2 | **Remove friction from the software development lifecycle** | Projects should automate something concrete – e.g., security fixes, code‑review assistance, compliance report generation, risk‑flagging, deployment pipelines, etc. |
| 3 | **Public, open‑source repository** | URL to a **public GitLab project** that contains all source code, assets, and clear licensing (primary license must be displayed at the top of the repo). |
| 4 | **Demo video ≤ 3 minutes** | Hosted publicly on YouTube or Vimeo; judges will only watch the first three minutes. |
| 5 | **Eligibility** – participant must be of legal age in their country of residence; all countries/territories allowed except “standard exceptions” (the usual sanction‑list exclusions). |
| 6 | **Access to the GitLab Duo Agent Platform** | Must **request access** to the “GitLab AI Hackathon group” (via the Discord channel or the provided sign‑up link). |
| 7 | **Compliance with Devpost rules** – follow the “Full Rules” link for legal and submission guidelines. |

> **Bottom line:**  *An eligible entry is a public GitLab repo that contains a working, trigger‑driven GitLab Agent (or Flow) that actually performs a useful automation, accompanied by a short demo and proper licensing.*

---

### 2️⃣ Judging Criteria & Relative Importance (inferred from prize structure)

| Category (Prize) | Cash Value | Points (Swag) | Implied Weight* |
|-------------------|------------|---------------|-----------------|
| **Grand Prize** (overall) | $15,000 | 1,000 pts | ★★★★★ (top priority) |
| **Most Technically Impressive** | $5,000 | 1,000 pts | ★★★★☆ |
| **Most Impactful** | $5,000 | 1,000 pts | ★★★★☆ |
| **Easiest to Use** | $5,000 | 1,000 pts | ★★★★☆ |
| **Most Impactful on GitLab & Google – Grand** | $10,000 | 500 pts | ★★★★☆ |
| **Most Impactful on GitLab & Google – Runner‑Up** | $3,500 | 500 pts | ★★★☆☆ |
| **Most Impactful on GitLab & Anthropic – Grand** | $10,000 | 500 pts | ★★★★☆ |
| **Most Impactful on GitLab & Anthropic – Runner‑Up** | $3,500 | 500 pts | ★★★☆☆ |
| **Green Agent Prize** | $3,000 | 500 pts | ★★★☆☆ (focus on sustainability) |
| **Sustainable Design Bonus** | $500 | 320 pts | ★★☆☆☆ |
| **Honorable Mention** | $500 (×6) | 320 pts each | ★★☆☆☆ |
| **Most Impactful on GitLab & Google – Runner‑Up** | $3,500 | 500 pts | ★★★☆☆ |

\*Weight is a qualitative interpretation: higher cash → higher judging emphasis. The “Grand Prize” and the two “Impactful on GitLab & Google/Anthropic” categories are the most heavily weighted, indicating judges will look for **overall excellence + deep integration with the named platform**.

**Key judging focus areas (derived from prize titles):**

1. **Technical depth / novelty** – code quality, agent architecture, integration with GitLab Duo.
2. **Impact** – measurable benefit to developers / reduction of friction.
3. **Usability** – clear UI/UX, easy onboarding, documentation.
4. **Platform‑specific impact** – extra points for leveraging **Google Cloud** or **Anthropic** APIs.
5. **Sustainability / Green** – low‑resource usage, eco‑friendly design.
6. **Design / polish** – overall presentation, demo quality, documentation.

---

### 3️⃣ Proprietary Platforms (account‑sign‑up required)

| Platform | Why it matters for the hackathon |
|----------|-----------------------------------|
| **GitLab Duo Agent Platform** | Core of the challenge – participants must request access, create agents/flows, and host code on GitLab. |
| **GitLab (hosted service)** | Repository hosting, CI/CD pipelines, and the Duo Agent runtime. |
| **Google Cloud** | Eligible for a $13,500 bonus prize; participants must have a Google Cloud account to call its services (e.g., Vertex AI, Cloud Functions). |
| **Anthropic** | Eligible for a $13,500 bonus prize; participants need an Anthropic API account (e.g., Claude) to power agents. |
| **Discord** (optional) | Used for community chat and “#ai-hackathon” channel – not a judging factor but required for community interaction. |

> **Action:**  Ensure each participant creates the necessary accounts **before** starting development, otherwise the “platform‑specific impact” prize categories are inaccessible.

---

### 4️⃣ Specific API / Access Keys Mentioned

The overview **does not list any concrete API keys or tokens**. It only references the need to use:

* Google Cloud APIs (you’ll need a Google Cloud API key / service‑account credentials).
* Anthropic APIs (you’ll need an Anthropic API key).

**No explicit key strings are provided** in the Devpost description, so teams must obtain their own keys after signing up for the respective services.

---

### 📋 Quick Checklist for Participants

| ✅ | Item |
|---|------|
| 1 | Sign‑up for **GitLab** and request access to the **GitLab AI Hackathon group** (Discord link). |
| 2 | (Optional but prize‑winning) Create accounts & obtain API keys for **Google Cloud** and/or **Anthropic**. |
| 3 | Build **≥ 1 public custom Agent or Flow** that reacts to GitLab events and performs a concrete automation. |
| 4 | Publish the full source in a **public GitLab repo** with a clearly visible license. |
| 5 | Write a concise **text description** of features/functionality. |
| 6 | Record a **≤ 3 min demo video** (YouTube/Vimeo, public). |
| 7 | Submit the project URL and accompanying assets on **Devpost** before **Mar 25 2026 @ 7 pm GMT+1**. |
| 8 | Highlight any **Google Cloud** or **Anthropic** integration in the submission to be eligible for the $13,500 bonus prizes. |
| 9 | Emphasize sustainability if targeting the **Green Agent** or **Sustainable Design** bonuses. |

--- 

**Overall Insight:**  The hackathon rewards not just raw technical chops, but *real‑world impact* and *deep integration* with the GitLab Duo Agent Platform plus optional cloud partners. Teams that ship a polished, trigger‑driven agent, clearly document it, and demonstrate measurable developer‑experience gains will score highest across the judging criteria.

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
*.log
*.pyc
.DS_Store
.aws/
.env
.gradient/
.idea/
.venv/
.vscode/
__pycache__/
build/
cdk.out/
coverage/
dist/
node_modules/
```

### requirements.txt Content:
```text
aiohttp
anthropic
google-cloud-aiplatform
gradient-adk
gradient-sdk
langgraph
pydantic
python-dotenv
python-gitlab
requests
rich
```

## 🚀 3. Proposed Concepts
## Idea 1 – **SecureMerge Bot**  
**What it does**  
A public **GitLab Duo Agent** that watches **Merge‑Request events** and automatically:  

1. Runs the built‑in GitLab SAST/DAST scanners.  
2. Sends the raw findings to **Anthropic Claude** (via Anthropic API) which translates each vulnerability into a short, developer‑friendly explanation plus a concrete code‑fix suggestion.  
3. Posts a single comment on the MR that contains:  
   * a risk rating,  
   * the AI‑generated remediation snippet, and  
   * a “✅ Approve if you trust the fix” button that, when clicked, triggers a **GitLab Flow** to apply the fix in a new branch and open a second MR.  

The whole workflow lives in a **public GitLab repo** (MIT‑licensed) and is demonstrated in a **≤ 3‑minute video**.

**Why it fits the hackathon**  

| Judging focus | How the bot scores |
|---|---|
| **Technical depth / novelty** | Combines Duo Agent triggers, GitLab’s native security scanners, and Anthropic LLM prompt‑engineering to auto‑rewrite code. |
| **Impact** | Cuts the “security‑fix friction” loop from days to minutes; developers see a ready‑to‑apply patch instead of a raw scanner dump. |
| **Usability** | Single‑click “Approve” button, no extra UI; all interactions happen inside the familiar MR view. |
| **Platform‑specific impact** | Direct Anthropic integration qualifies for the **$13.5 k “Most Impactful on GitLab & Anthropic”** prize. |
| **Sustainability** | Runs only on MR events; minimal compute time – low carbon footprint (bonus for Green Agent). |
| **Polish** | Demo shows the MR lifecycle, the comment, the auto‑generated fix, and the final merged result. |

---

## Idea 2 – **EcoDeploy Scheduler**  
**What it does**  
A public **GitLab Duo Flow** that sits between CI pipeline completion and production deployment:  

1. Listens for **pipeline‑finished** events on the `staging` environment.  
2. Calls **Google Cloud’s Carbon‑Aware Computing API** to fetch the latest carbon intensity forecast for all supported GCP regions.  
3. If the current region’s forecast exceeds a configurable threshold, the flow automatically **re‑routes the deployment** to the greener region *or* schedules the deployment to the next low‑intensity time‑window (via Cloud Scheduler).  
4. Posts an immutable **“Green‑Deployment Report”** comment on the pipeline with carbon‑saved estimate and a link to the GCP console.  

All code lives in a **public GitLab repository** (Apache‑2.0) with a short demo video illustrating a pipeline being postponed to a greener slot.

**Why it fits the hackathon**  

| Judging focus | How the flow scores |
|---|---|
| **Technical depth / novelty** | Bridges GitLab CI events, Google Cloud carbon‑aware APIs, and automated rescheduling of deployments. |
| **Impact** | Directly reduces the carbon cost of each release; teams can quantify saved kg CO₂ e. |
| **Usability** | No manual steps – developers just merge; the flow handles scheduling transparently. |
| **Platform‑specific impact** | Uses **Google Cloud** services → eligible for the **$13.5 k “Most Impactful on GitLab & Google”** prize. |
| **Green Agent prize** | Core purpose is sustainability; qualifies for the $3 k “Green Agent” and the $500 “Sustainable Design” bonus. |
| **Polish** | Demo includes the carbon forecast UI, the automatic region switch, and the final green‑deployment badge. |

---

## Idea 3 – **Compliance‑Doc Builder**  
**What it does**  
A public **GitLab Duo Agent** that creates a **ready‑to‑share compliance report** every time code is pushed to the `main` branch:  

1. Triggers on **push** events.  
2. Scans the repository with GitLab’s **Security & License Scanning** and **IaC (Terraform/Kubernetes) policies**.  
3. Sends the raw findings to a **Google Cloud Function** that uses **Document AI** to format them into a clean PDF (sections: security findings, license mismatches, infra‑as‑code policy violations).  
4. Commits the PDF back to a `compliance/` folder and adds a comment on the push with a download link.  

The entire system is open‑source (BSD‑3‑Clause) and showcased in a 3‑minute demo that walks through a push, the generated PDF, and the automatic commit.

**Why it fits the hackathon**  

| Judging focus | How the agent scores |
|---|---|
| **Technical depth / novelty** | Marries Duo Agent event handling, GitLab scanning, and Google Document AI for polished reporting. |
| **Impact** | Eliminates manual compliance‑report generation, saving hours for security & ops teams. |
| **Usability** | One‑time setup; after that the PDF appears automatically in the repo – developers just keep coding. |
| **Platform‑specific impact** | Uses **Google Cloud** APIs → qualifies for the Google‑focused impact prizes. |
| **Sustainability** | Runs only on push events; lightweight processing, low compute cost. |
| **Polish** | Demo highlights the PDF layout, the automatic commit, and a quick glance at the compliance summary. |

---

### Quick sanity check against mandatory requirements  

| Requirement | Covered by each idea |
|---|---|
| **1️⃣ Custom public agent/flow** | SecureMerge Bot (Agent), EcoDeploy Scheduler (Flow), Compliance‑Doc Builder (Agent) |
| **2️⃣ Remove friction from SDLC** | All three automate a concrete step (security fix, green deployment, compliance reporting). |
| **3️⃣ Public open‑source repo** | Each idea explicitly mentions a public GitLab repo with a standard OSS license. |
| **4️⃣ Demo ≤ 3 min** | All ideas are scoped for a concise three‑minute walkthrough. |
| **5️⃣ Eligibility** | No restriction beyond standard rules – all ideas are universally eligible. |
| **6️⃣ Access to Duo Agent Platform** | Assumed by participants; each project is built on that platform. |
| **7️⃣ Devpost compliance** | The project descriptions include all required assets for a proper Devpost submission. |

These concepts keep the implementation lightweight (single‑event trigger → API call → actionable output) while still hitting the high‑value judging categories (technical depth, impact, platform integration, sustainability). Choose the one that best matches your team’s skill‑set and the prize you’re targeting!
            