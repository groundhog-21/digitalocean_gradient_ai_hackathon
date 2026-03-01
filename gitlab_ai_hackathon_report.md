
# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
**GitLab AI Hackathon – Structured Setup Summary**

---

## 1. Mandatory Requirements (Must‑Builds)

| # | Requirement | Details / Acceptance Criteria |
|---|-------------|--------------------------------|
| **1** | **Agent‑type solution** | Must be an **AI Agent** (not just a chat‑bot) that **reacts to triggers/events** and **takes action** within the GitLab workflow. |
| **2** | **Public custom agent or flow** | At least **one custom *public* agent OR a public flow** must be created and published in the “GitLab AI Hackathon group”. |
| **3** | **Scope of the agent** | Must **remove friction** from any stage of the software development lifecycle (e.g., security fixes, code‑review automation, compliance report generation, risk‑flagging, test creation, deployment orchestration, etc.). |
| **4** | **Open‑source repository** | Submit a **public GitLab repository** containing **all source code, assets and instructions**. The primary license must be **clearly visible** in the “Project information” section. |
| **5** | **Project description** | Provide a **text description** (README) that explains the features, functionality and the pain point the agent solves. |
| **6** | **Demo video** | Upload a **max‑3‑minute demo video** to **YouTube or Vimeo** (public) and include the link in the submission. |
| **7** | **Eligibility** | Participants must be **of legal age** in their country of residence. All countries/territories are allowed **except standard exclusions** (see full rules). |
| **8** | **Access to platform** | Teams must **request access** to the **GitLab Duo Agent Platform** (via the provided “Request Access” link) before building. |

> **Bottom‑line “Must‑Build”** – *A publicly‑available, trigger‑driven GitLab AI Agent (or Flow) that automates a concrete developer workflow, hosted in a licensed open‑source repo with a short public demo video.*

---

## 2. Judging Criteria & Relative Importance

| Category (Prize) | Cash Value | Points (Swag) | Primary Judging Focus | Relative Weight* |
|------------------|------------|---------------|-----------------------|------------------|
| **Grand Prize** | $15,000 | 1 000 | Overall impact, innovation, completeness, scalability | **Highest** |
| **Most Technically Impressive** | $5,000 | 1 000 | Technical depth, clever use of AI/agent APIs, engineering quality | High |
| **Most Impactful** | $5,000 | 1 000 | Measurable benefit to developers / workflow efficiency | High |
| **Easiest to Use** | $5,000 | 1 000 | UI/UX, onboarding simplicity, documentation clarity | High |
| **Honorable Mention** | $500 | 320 | Notable effort, creative angle, may not meet top‑tier criteria | Medium |
| **Sustainable Design Bonus** | $500 | 320 | Eco‑friendly compute, minimal resource usage, green engineering | Medium |
| **Most Impactful on GitLab & Google – Grand** | $10,000 | 500 | Deep integration with **Google Cloud** services, measurable impact on GitLab + GCP workflow | High |
| **Most Impactful on GitLab & Google – Runner‑up** | $3,500 | 500 | Same as above but secondary tier | Medium‑High |
| **Most Impactful on GitLab & Anthropic – Grand** | $10,000 | 500 | Deep integration with **Anthropic** LLMs via GitLab, strong impact on GitLab workflow | High |
| **Most Impactful on GitLab & Anthropic – Runner‑up** | $3,500 | 500 | Same as above, runner‑up level | Medium‑High |
| **Green Agent Prize** | $3,000 | 500 | Agents that **reduce carbon footprint** (e.g., low‑compute models, efficient pipelines) | Medium‑High |
| **Additional prize pool for platform use** | $13,500 (Google Cloud) + $13,500 (Anthropic) + $3,000 (Green) | – | **Incentive** to use the named proprietary platforms; judges will look for proper integration | Adds weight to the above platform‑specific categories |

\*Weight is inferred from cash amount and the fact that categories with higher prize values are generally judged more stringently.

---

## 3. Proprietary Platforms (Account‑Sign‑Up Required)

| Platform | Why Needed | Typical Sign‑Up / Access Step |
|----------|------------|------------------------------|
| **GitLab Duo Agent Platform** | Core SDK/API for building custom agents & flows. | Request access via the “Request Access to the GitLab AI Hackathon group” link (GitLab account required). |
| **Google Cloud Platform (GCP)** | Eligible for $13.5 k prize pool; used for hosting, AI services, storage, CI/CD, etc. | GCP account + billing (free tier may suffice) + enable required APIs. |
| **Anthropic** (Claude/other LLM) | Eligible for $13.5 k prize pool; used as LLM provider through GitLab integration. | Anthropic API account → obtain API key. |
| **Discord** (community channel) | Communication & announcements. | Discord account + join the hackathon server. |
| **YouTube / Vimeo** (demo video hosting) | Required for demo video upload. | Free account on either platform. |

> **Note:** No DigitalOcean, AWS, Azure, or other cloud providers are mentioned as mandatory, but participants are free to use any services as long as they meet the prize‑specific criteria.

---

## 4. Specific API / Access Keys Mentioned

The hackathon description **does not publish literal API keys**, but the following **keys/credentials are implicitly required** for successful participation:

| Needed Credential | Where It Is Used | How To Obtain |
|-------------------|------------------|----------------|
| **GitLab Personal Access Token (PAT)** | Authenticating with the GitLab Duo Agent Platform, creating agents/flows, pushing code to the hackathon group. | Generate in GitLab user settings → *Access Tokens*. |
| **Google Cloud API key / Service Account JSON** | Accessing GCP services (e.g., Cloud Functions, Vertex AI, Cloud Storage) for the Google‑specific prize track. | Create a service account in GCP console, download JSON key, enable relevant APIs. |
| **Anthropic API key** | Calling Anthropic LLMs from within an agent for the Anthropic‑specific prize track. | Sign up at `anthropic.com`, generate an API key in the dashboard. |
| **Discord OAuth token** (optional) | If a bot or webhook integration is built for Discord notifications. | Create a Discord application → bot token. |
| **YouTube/Vimeo API key** (optional) | If the submission programmatically uploads the demo video. | Obtain via Google Cloud console (YouTube) or Vimeo developer portal. |

> No hard‑coded example keys are listed in the overview; participants must **request or generate** their own credentials.

---

## 5. Quick “Cheat‑Sheet” for Teams

| Step | Action | Platform / Resource |
|------|--------|---------------------|
| 1 | **Create / verify GitLab account** & generate a **PAT**. | GitLab |
| 2 | **Request access** to the **GitLab Duo Agent Platform** (hackathon group). | GitLab |
| 3 | **Choose a prize track** (Google Cloud, Anthropic, Green) → set up the corresponding account & obtain API keys. | GCP / Anthropic |
| 4 | **Design & build** a **public custom agent or flow** that reacts to GitLab events. | GitLab Duo SDK |
| 5 | **Host the full source** in a **public repository** inside the hackathon group, with a clear license. | GitLab |
| 6 | Write a concise **README** describing the pain point, solution, and usage. | GitLab |
| 7 | Record a **≤ 3‑minute demo** → upload to **YouTube/Vimeo** (public) → capture the link. | YouTube/Vimeo |
| 8 | Submit the **project URL**, **description**, and **demo video link** on Devpost before **Mar 25 2026 7 pm GMT+1**. | Devpost |
| 9 | (Optional) Join the **Discord server** for community help and updates. | Discord |
| 10 | Highlight any **environment‑friendly** design choices if targeting the **Green Agent** or **Sustainable Design** bonuses. | – |

---

### Bottom Line
- **Must‑build:** a trigger‑driven, public GitLab AI Agent (or Flow) that automates a real developer workflow.
- **Judging:** weighted heavily toward overall impact & technical depth, with extra cash for integrations with **Google Cloud**, **Anthropic**, and **green** design.
- **Proprietary platforms:** GitLab Duo, Google Cloud, Anthropic (all require individual sign‑ups and API keys).  
- **No explicit API keys** are published; teams must provision their own credentials.  

Good luck, and happy hacking!

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
*.bak
*.log
*.pyc
*.sqlite
*.tmp
.DS_Store
.aws/
.cache/
.env
.gradient/
.idea/
.mypy_cache/
.pytest_cache/
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
anthropic
flask
gitlab
google-cloud-aiplatform
google-cloud-pubsub
google-cloud-storage
gradient-adk
gradient-sdk
langgraph
pydantic
python-dotenv
requests
```

## 🚀 3. Proposed Concepts
## Idea 1 – **AutoSec‑Fixer Agent**

**Description**  
An AI Agent that watches **`push`** events on any repository.  
1. As soon as new code lands, the agent runs a lightweight static‑security scanner (e.g., Bandit or CodeQL).  
2. When a vulnerability is found, the agent calls **Anthropic Claude** to generate a minimal, context‑aware fix (‑‑‑ “replace this insecure function with a safe alternative”).  
3. The generated patch is applied to a **temporary branch**, a **merge‑request** is opened, and the developer receives a notification (Discord/Slack webhook).  
4. If the MR is approved, the agent can optionally auto‑merge after a final CI pass.

**Why it fits**  
| Requirement | How the idea satisfies it |
|-------------|----------------------------|
| **Agent‑type solution** | Reacts to `push` events, performs analysis, creates MR – full “agent” behavior, not a simple chatbot. |
| **Public custom agent or flow** | The agent code is published as a **public GitLab AI Agent** in the hackathon group. |
| **Scope – remove friction** | Eliminates manual security‑review steps; developers get instant, auto‑generated fixes. |
| **Open‑source repo & license** | All source, Dockerfile, and a `LICENSE` (MIT) are hosted publicly. |
| **README & demo video** | README explains the workflow, how to enable the agent, and shows a 2‑min demo of a vulnerability being auto‑fixed. |
| **Technical depth** | Uses Anthropic LLM for code‑generation, integrates static‑analysis tools, and manipulates GitLab MR API – good for “Most Technically Impressive”. |
| **Impact** | Cuts security‑fix turnaround from days to minutes → strong for “Most Impactful”. |
| **Ease of use** | One‑line `gitlab-runner` registration + optional UI toggle in project settings → qualifies for “Easiest to Use”. |
| **Anthropic prize track** | Direct integration with Claude (LLM) makes it a prime candidate for **Most Impactful on GitLab & Anthropic**. |
| **Green design** | Runs the scanner and LLM only on changed files; uses low‑compute Claude `claude‑instant‑1.2` model → qualifies for the **Green Agent** bonus. |

---

## Idea 2 – **Deploy‑Optimizer Agent**

**Description**  
A trigger‑driven agent that turns a successful pipeline into a **cost‑aware, auto‑scaled deployment** on **Google Cloud Run** (or Cloud Functions).  

1. On a **`pipeline_success`** event for a `staging` branch, the agent builds a container image (using Cloud Build) and pushes it to **Artifact Registry**.  
2. The agent then deploys the image to a **temporary Cloud Run service** with a **pre‑configured auto‑shutdown timer** (e.g., 30 min idle).  
3. A short status comment is posted on the pipeline, and a **Discord webhook** shares the live preview URL.  
4. When the next commit lands, the old service is automatically **replaced**, so only one short‑lived environment ever runs.  

**Why it fits**  
| Requirement | How the idea satisfies it |
|-------------|----------------------------|
| **Agent‑type solution** | Reacts to `pipeline_success` events, launches cloud resources, and cleans them up – full action‑taking agent. |
| **Public custom agent or flow** | The full agent (Python + GitLab Duo SDK) is published publicly in the hackathon group. |
| **Scope – remove friction** | Gives developers an instant, disposable “preview” environment without manual GCP steps. |
| **Open‑source repo & license** | Hosted on GitLab with an Apache‑2.0 license, plus Terraform scripts for GCP resources. |
| **README & demo video** | Step‑by‑step instructions and a ≤3‑min video showing a commit → preview URL → auto‑teardown. |
| **Google Cloud prize track** | Deploys to Cloud Run, uses Cloud Build, and stores images in Artifact Registry → perfect for **Most Impactful on GitLab & Google** (Grand or Runner‑up). |
| **Technical depth** | Orchestrates multiple GCP services via their SDKs, handles auth, and manages lifecycle – strong for “Most Technically Impressive”. |
| **Impact** | Removes the “environment‑setup” bottleneck, speeds up QA cycles → high impact score. |
| **Ease of use** | After one‑time GCP service‑account setup, the agent is enabled with a single checkbox in project settings. |
| **Sustainable design** | The auto‑shutdown timer guarantees resources run only when needed, cutting compute‑hour waste → qualifies for **Green Agent** and **Sustainable Design Bonus**. |

---

## Idea 3 – **Compliance‑Snap Agent**

**Description**  
An agent that automatically generates a **regulatory‑compliance snapshot** every time a merge request is merged.  

1. Trigger: **`merge_request_merged`** event.  
2. The agent pulls the diff, extracts metadata (author, changed files, dependencies).  
3. Using **Anthropic Claude** it drafts a concise compliance narrative (e.g., GDPR, SOC‑2) summarizing the change, risk level, and required follow‑up.  
4. The narrative is saved as a **PDF** in a **Google Cloud Storage bucket** (public‑read for auditors) and a markdown version is posted as a comment on the MR.  
5. Optionally, the agent can raise a GitLab issue if the AI flags a high‑risk change.

**Why it fits**  
| Requirement | How the idea satisfies it |
|-------------|----------------------------|
| **Agent‑type solution** | Reacts to MR merge, calls LLM, writes files, creates issues – full automation flow. |
| **Public custom agent or flow** | The entire flow (GitLab Duo + Cloud Functions) is publicly released. |
| **Scope – remove friction** | Automates tedious compliance documentation, saving legal/ops teams hours per release. |
| **Open‑source repo & license** | Hosted publicly with a BSD‑3‑Clause license and clear contribution guidelines. |
| **README & demo video** | Includes a walkthrough of a merge → PDF generation → issue creation (≈2 min video). |
| **Anthropic integration** | Uses Claude for natural‑language compliance drafting → eligible for **Anthropic impact** prizes. |
| **Google Cloud integration** | Stores artifacts in GCS, optionally uses Cloud Functions → qualifies for **Google impact** categories as well. |
| **Impact** | Directly reduces manual compliance effort and improves audit traceability – high impact. |
| **Ease of use** | Once the service‑account key is added to project variables, the agent works automatically; no extra UI needed. |
| **Green design** | Runs only once per merge and uses the low‑compute Claude‑instant model; storage is cheap and long‑term – fits the **Green Agent** bonus. |

---

### Quick Takeaway
*All three concepts are **trigger‑driven GitLab AI Agents**, published publicly with open‑source licenses, include a README and a ≤3‑minute demo video, and can be built using the required Duo Agent SDK. They each hit a different high‑value prize track (Anthropic, Google Cloud, Green) while staying simple enough to prototype within a hackathon weekend.*
            