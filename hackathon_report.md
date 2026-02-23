
# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
**GitLab AI Hackathon – Structured Setup Summary**

---  

### 1. Mandatory Requirements (Must‑Builds)

| # | Requirement | Details / How to satisfy |
|---|-------------|--------------------------|
| **1** | **Create at least ONE custom **public** agent **or** public flow** | Must be built on the **GitLab Duo Agent Platform**. “Public” means the code is visible to anyone (no private repos). |
| **2** | **Agent must be event‑driven** – react to triggers & take action | Pure chat‑only bots are disqualified. The agent should listen to GitLab webhook events (e.g., merge‑request opened, pipeline failed) and perform automated tasks (e.g., generate tests, run security scans, create compliance reports). |
| **3** | **All submissions must be open‑source** | Repository URL must be publicly accessible, contain a detectable license (displayed at the top of the repo’s Project Information section). |
| **4** | **Submission package** – three mandatory artefacts<br>• **Repo URL** (with full source, assets, README)<br>• **Text description** of features/functionality<br>• **Demo video** (≤ 3 min, hosted publicly on YouTube or Vimeo) | The demo video is the only visual judge input; it must be public and limited to 3 minutes. |
| **5** | **Eligibility** – be of legal age in your country & not belong to any “standard exceptions” (the usual sanction‑list countries). |
| **6** | **Access request** – obtain permission to the **GitLab Duo Agent Platform** and to the **GitLab AI Hackathon group** (via the “Request Access” link). |
| **7** | **Optional “bonus” tracks** – to unlock extra prize pools you must *use* the indicated platform(s):<br>• Google Cloud ( $13,500  prize pool) <br>• Anthropic via GitLab ( $13,500  prize pool) <br>• “Green Agents” ( $3,000  prize pool) | Participation in a bonus track is not mandatory for the base prize, but you must actually provision and use the respective service in your agent/flow. |

---  

### 2. Judging Criteria & Relative Importance  

| Category (Prize) | Primary Focus (What judges will look for) | Relative Weight (≈ Prize Money) |
|------------------|--------------------------------------------|---------------------------------|
| **Grand Prize** – $15 k | Overall excellence: innovation, impact, technical depth, usability, and alignment with GitLab’s vision. | **Highest** (baseline) |
| **Most Technically Impressive** – $5 k | Depth of AI/ML engineering, algorithmic novelty, robust integration with GitLab APIs, performance. | High |
| **Most Impactful** – $5 k | Real‑world benefit to developers, measurable friction reduction, adoption potential. | High |
| **Easiest to Use** – $5 k | UI/UX clarity, clear documentation, low learning curve, smooth onboarding. | High |
| **Most Impactful on GitLab & Google – Grand** – $10 k | Same as “Most Impactful” *plus* demonstrable use of Google Cloud services (e.g., Vertex AI, Cloud Functions). | Very High (specific platform focus) |
| **Most Impactful on GitLab & Google – Runner‑up** – $3.5 k | Same as above but second‑place. | Medium‑High |
| **Most Impactful on GitLab & Anthropic – Grand** – $10 k | Same as “Most Impactful” *plus* integration of Anthropic models via GitLab. | Very High (specific platform focus) |
| **Most Impactful on GitLab & Anthropic – Runner‑up** – $3.5 k | Same as above, second‑place. | Medium‑High |
| **Green Agent Prize** – $3 k | Sustainability: low‑carbon compute, efficient resource usage, eco‑friendly design patterns. | Medium |
| **Honorable Mention** – $500 (×6) | Projects that are solid but don’t dominate any single category; overall quality. | Low‑Medium |
| **Sustainable Design Bonus** – $500 (×4) | Specific attention to design for longevity, maintainability, and minimal waste. | Low‑Medium |
| **Points (Swag) prizes** (1 000 pts or 320 pts) | Not monetary; used for internal GitLab swag store. | Supplemental |

**Interpretation:**  
- **Technical depth + platform‑specific integration** yields the largest cash awards (Grand, GitLab & Google/Anthropic).  
- **Usability & impact** are heavily weighted (Most Impactful, Easiest to Use).  
- **Sustainability** is rewarded but at lower cash levels (Green Agent, Sustainable Design).  

---  

### 3. Proprietary Platforms Requiring Account Sign‑Ups  

| Platform | Reason for sign‑up / access | What you’ll need |
|----------|-----------------------------|------------------|
| **GitLab Duo Agent Platform** | Core hackathon platform (agents/flows) – requires being added to the “GitLab AI Hackathon” group. | GitLab account + request access (via provided link). |
| **GitLab (hosted)** | Repo hosting, CI/CD, webhooks, API keys for agent actions. | Standard GitLab account; generate **Personal Access Token** for API calls (not supplied in the brief). |
| **Google Cloud** (optional bonus) | Use of GCP services (Vertex AI, Cloud Functions, etc.) to earn $13.5k bonus. | Google Cloud account; enable billing; create service account & API keys. |
| **Anthropic** (optional bonus) | Access to Anthropic’s Claude models through GitLab integration for $13.5k bonus. | Anthropic API key (to be provisioned after signing up on Anthropic’s portal). |
| **YouTube / Vimeo** | Host the required demo video (public). | Normal user account on either platform. |
| **Discord** (community) | Join #ai-hackathon channel for networking; not strictly required for the build. | Discord account. |

---  

### 4. Specific API / Access Keys Mentioned  

- **None** are explicitly listed in the overview.  
- Implicitly required keys/tokens:  
  - **GitLab Personal Access Token** (for the agent to call GitLab APIs).  
  - **Google Cloud Service‑Account JSON key** (if you pursue the Google Cloud bonus).  
  - **Anthropic API key** (if you pursue the Anthropic bonus).  

> *Action:* Teams must generate these credentials themselves after obtaining the necessary platform accounts; they are not pre‑provided by the hackathon organizers.

---  

### 5. Quick “What‑to‑Do” Checklist for Participants  

1. **Set up accounts** – GitLab (enable Duo Agent Platform access), optional Google Cloud & Anthropic accounts.  
2. **Generate required tokens** – GitLab PAT, GCP service‑account key, Anthropic API key (if using).  
3. **Create a public GitLab repo** with a clear LICENSE header (visible on the repo page).  
4. **Build at least one public agent or flow** that **listens to GitLab events** and **takes automated action** (not just chat).  
5. **If targeting a bonus track**, integrate the relevant platform (GCP services or Anthropic models).  
6. **Write a concise README** describing problem, solution, trigger/action flow, and any platform usage.  
7. **Record a ≤ 3‑minute demo** (public YouTube/Vimeo) showing the agent in action.  
8. **Submit the repo URL, description, and video link** before the deadline (Mar 25 2026 @ 19:00 GMT+1).  
9. **Optional** – join the Discord #ai-hackathon channel for support & networking.  

---  

**End of Summary**.

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
*.log
*.pyc
*.tmp
.DS_Store
.aws/
.env
.gradient/
.venv/
__pycache__/
cdk.out/
dist/
node_modules/
```

### requirements.txt Content:
```text
anthropic
flask
google-cloud-aiplatform
gradient-adk
gradient-sdk
langgraph
python-dotenv
python-gitlab
requests
```

## 🚀 3. Proposed Concepts
---

## 1. **Merge‑Guard: Auto‑Review & Security‑Gate Agent**  

**Description**  
A public GitLab Duo **agent** that watches three core web‑hook events:  

| Trigger | Action |
|---------|--------|
| `merge_request.opened` | • Run a lightweight static‑analysis suite (ESLint, Bandit, etc.) <br>• Summarize findings with a concise comment on the MR <br>• Attach a “Compliance badge” (✅/⚠️) |
| `pipeline.failed` | • Pull the failure logs, run an **AI‑generated root‑cause analysis** using Anthropic Claude (via the GitLab‑Anthropic integration) <br>• Post a comment with a step‑by‑step remediation plan |
| `release.created` | • Auto‑generate a **SBOM** (Software Bill‑of‑Materials) with CycloneDX, store it as an artifact, and add a public link to the release notes |

All logic lives in a **single, public repo** (MIT licence) and the agent is deployed as a **GitLab Cloud Run‑like function** (uses GitLab‑hosted CI jobs to keep the runtime on GitLab’s infrastructure → low‑carbon). The README ships with a one‑click “Enable this agent on your project” button that creates the needed webhook and secret token.

**Why it fits**  

| Requirement | How it is satisfied |
|-------------|---------------------|
| **Public agent / flow** | Fully open‑source repo, visible code, License header. |
| **Event‑driven** | Reacts to MR open, pipeline failure, and release creation – never a pure chat bot. |
| **Open‑source** | MIT licence, auto‑displayed on GitLab project page. |
| **Submission artefacts** | Repo URL, a 2‑minute demo video (MR opening → comment posted), and a short feature list in the README. |
| **Bonus track (Anthropic)** | Uses Claude to generate natural‑language remediation; qualifies for the **Anthropic $13.5k** prize. |
| **Easiness** | One‑click install, zero‑config comment templates, clear docs → strong “Easiest to Use” potential. |
| **Impact** | Cuts review latency, surfaces security findings instantly → high “Most Impactful”. |
| **Green** | Runs entirely on GitLab CI (shared runners) → low‑carbon footprint, qualifies for the **Green Agent** prize. |

---

## 2. **Git‑Docs‑Bot: Auto‑Docs & Knowledge‑Base Publisher (Google Cloud)**  

**Description**  
A public **flow** that triggers on `push` events to any repository containing a `README.md` or `docs/` folder. The flow performs:  

1. **Extract** all markdown files and feed them to **Vertex AI PaLM 2** (Google Cloud) to generate a concise **FAQ** and **architecture diagram** (via Mermaid).  
2. **Publish** the generated assets to a **public Google Cloud Storage bucket** (static‑site hosting) and push a link back to the originating project as a comment.  
3. **Cache** the AI‑generated outputs in **Firestore** to avoid re‑processing unchanged files (cost‑effective & sustainable).  

The entire pipeline is defined as a **GitLab CI YAML** that calls a **Google Cloud Function** (written in Python) – the function is the only piece of code you need to keep public (in the same repo). The demo shows a push, the AI‑enhanced docs appear on a public URL within seconds.

**Why it fits**  

| Requirement | How it is satisfied |
|-------------|---------------------|
| **Public agent / flow** | All code (CI YAML, Cloud Function) lives in a public GitLab repo under an Apache‑2.0 licence. |
| **Event‑driven** | Triggered by GitLab `push` webhook; never a standalone chatbot. |
| **Open‑source** | License header visible; repo searchable. |
| **Submission artefacts** | Repo URL, a 2‑minute demo video (push → docs published), and a concise description file. |
| **Bonus track (Google Cloud)** | Uses Vertex AI, Cloud Functions, Firestore, and GCS → qualifies for the **GitLab & Google Grand** $10k prize (and potentially the runner‑up). |
| **Easiest to Use** | One‑click “Enable Docs Bot” button adds the webhook and creates the GCP resources via Terraform scripts; users only need to grant a service‑account JSON. |
| **Impact** | Provides instant, AI‑enhanced documentation without developer effort – a huge friction reducer → “Most Impactful”. |
| **Green** | Cloud Function runs only when needed; Firestore caching minimizes API calls → low carbon usage, eligible for the **Green Agent** prize. |

---

## 3. **Eco‑Pipeline‑Watcher: Carbon‑Aware CI Optimizer**  

**Description**  
A public **agent** that monitors `pipeline.started` and `pipeline.finished` events. Its responsibilities:  

* **Estimate** the carbon intensity of the compute region (via Google Cloud’s Carbon Footprint API or a public dataset).  
* **Analyze** the pipeline duration and resource usage (CPU, memory).  
* **Suggest** greener alternatives:  
  * Switch to a lower‑intensity region (auto‑create a MR with a modified `.gitlab-ci.yml`).  
  * Replace heavyweight Docker images with **distroless** versions.  
* **Log** weekly sustainability reports to a public GitLab Markdown page in the repo (`SUSTAINABILITY.md`).  

The agent is a lightweight **Node.js** service deployed on **GitLab’s own serverless runner** (no external cloud required). The repo includes a small dashboard (HTML + Chart.js) that reads the markdown report via the GitLab API and visualizes carbon savings over time.

**Why it fits**  

| Requirement | How it is satisfied |
|-------------|---------------------|
| **Public agent** | All source files (Node service, dashboard) are in a public GitLab repo under a BSD‑3‑Clause licence. |
| **Event‑driven** | Reacts to `pipeline.started` and `pipeline.finished` webhooks only. |
| **Open‑source** | License visible, fully reproducible. |
| **Submission artefacts** | Repo URL, a 2‑minute video showing a pipeline run → carbon estimate comment, and a description in the README. |
| **Green Agent prize** | Explicit focus on carbon‑aware decisions, runs on shared runners → strong contender for the **$3k Green Agent** prize. |
| **Impact** | Directly reduces the carbon footprint of CI/CD— measurable savings → “Most Impactful”. |
| **Easiest to Use** | One‑line `curl` command to register the webhook + optional auto‑setup script; minimal configuration. |
| **Technical depth** | Combines real‑time webhook handling, external carbon‑intensity API, and automated MR generation → also a good fit for “Most Technically Impressive”. |

---
            