# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
**Amazon Nova AI Hackathon – Structured Setup Data**

| Category | Details |
|----------|---------|
| **1️⃣ Mandatory Requirements (Must‑Builds)** | • **Core tech** – Your solution **must** use **Amazon Nova** (any of the listed foundation models or the Nova Act service).  <br> - Nova 2 Lite (reasoning) <br> - Nova 2 Sonic (speech‑to‑speech) <br> - Nova multimodal Embeddings <br> - Nova Act (agent fleet / UI‑workflow automation) <br>• **Scope** – Build a **generative AI application** on **AWS** that leverages one (or more) of the above. <br>• **Allowed focus categories** (you may pick any, or “Freestyle”):  <br> - Agentic AI  <br> - Multimodal Understanding  <br> - UI Automation (Nova Act)  <br> - Voice AI (Nova 2 Sonic)  <br> - Freestyle  <br>• **Submission artefacts** – Text description, ≤3 min demo video (include #AmazonNova), code repo link (public or private – if private give access to `testing@devpost.com` and `Amazon‑Nova‑hackathon@amazon.com`). |
| **2️⃣ Judging Criteria & Weighting** | |<u>Primary Hackathon Submission</u>| |<u>Optional Feedback / Blog‑Post Submissions</u>| |
| – Technical Implementation | **60 %** – quality, effectiveness, integration with Amazon Nova, overall system architecture. |
| – Enterprise or Community Impact | **20 %** – business value or tangible community benefit. |
| – Creativity & Innovation | **20 %** – novelty of approach, innovative use of multi‑agent systems, real‑world problem solving. |
| – Feedback Submission (optional) | Evaluated on **completeness, viability, potential impact** of the feedback itself. |
| – Blog‑Post Prize (optional) | Evaluated on **completeness and potential impact** of the post (how the project benefits the target community, adoption plan, etc.). |
| **3️⃣ Proprietary Platforms (account required)** | • **Amazon Web Services (AWS)** – Needed to provision Nova models/services. <br>• **Amazon Nova** (accessed through AWS console/API). <br>• **Devpost** – Required for hackathon registration, project submission, and private‑repo access permissions. |
| **4️⃣ Specific API / Access Keys Mentioned** | None are listed in the overview.  (Access to Nova models will be via standard AWS credentials; participants must have an AWS account and appropriate IAM permissions, but no hard‑coded keys are provided in the rules.) |
| **5️⃣ Other Notable Logistics** | • **Eligibility** – Ages 18+, certain countries/territories excluded (full list in “View full rules”). <br>• **Prize pool** – $40 k cash + $55 k AWS credits (plus many category‑specific awards). <br>• **Deadline** – 17 Mar 2026 @ 01:00 am GMT+1 (online, public). <br>• **Required tags in demo** – Include the hashtag **#AmazonNova**. |

---  

**Take‑away for participants**  
1. **Secure an AWS account** (and enable the Amazon Nova APIs).  
2. **Design your project around at least one Nova foundation model or Nova Act** – this is non‑negotiable.  
3. **Focus on the three weighted criteria** (Technical Implementation > Impact > Creativity) to maximise your score.  
4. **Prepare a short demo video with the #AmazonNova tag** and ensure any private repo is shared with the two email addresses listed.  
5. **Optional bonuses** (blog post, feedback survey) can earn extra AWS credits or cash – follow the separate judging rubrics.  

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
*.log
*.pyc
*.tfstate
.DS_Store
.aws/
.coverage
.env
.gradient/
.idea/
.pytest_cache/
.terraform/
.venv/
.vscode/
__pycache__/
cdk.out/
coverage/
node_modules/
```
### requirements.txt Content:
```text
boto3
gradient-adk
gradient-sdk
langgraph
numpy
opencv-python
pandas
pillow
pydub
python-dotenv
requests
tqdm
transformers
```
## 🚀 3. Proposed Concepts (Singles & Doubles)
## 1️⃣ Idea: **Nova‑Tutor – AI Study‑Planner & Homework Helper**  
**Category:** Agentic AI + UI Automation (Nova‑Act)  

### Description  
- **Frontend:** A lightweight web app (React + Amplify) where students type a “What do I need to learn this week?” prompt.  
- **Core Engine:**  
  1. **Nova‑2‑Lite** generates a structured weekly syllabus, breaks topics into bite‑size lessons, and writes short quiz questions.  
  2. **Nova‑Act** orchestrates a multi‑step workflow:  
     * Pulls free‑open‑source video / article links from AWS‑OpenSearch,  
     * Populates a personalized Notion/Google‑Docs template via the respective APIs,  
     * Sends a reminder email (SES) each evening.  
- **Output:** A downloadable PDF + an interactive checklist that updates automatically as the student marks tasks complete.  

### Why it fits  

| Requirement | How it’s met |
|-------------|--------------|
| **Core tech** | Uses **Nova‑2‑Lite** for reasoning and **Nova‑Act** for agentic UI‑automation. |
| **Scope** | A generative AI app built on AWS (Amplify, Lambda, SES, OpenSearch). |
| **Simplicity** | Only two Nova services; the workflow is a linear “plan → fetch resources → push to doc”. |
| **Impact** | Direct community benefit for students & lifelong learners (20 % impact score). |
| **Technical depth** | Shows effective prompting, multi‑agent orchestration, integration with external SaaS – strong 60 % technical score. |
| **Creativity** | Combines AI‑generated syllabus with automated document creation – a novel “AI‑teacher‑assistant” niche. |

---

## 2️⃣ Idea: **Voice‑Summarize – Real‑Time Meeting Minutes Generator**  
**Category:** Voice AI + Multimodal Understanding  

### Description  
- **Capture:** Participants join a simple AWS Chime‑style web UI and press “Start”. Audio streams to **Nova‑2‑Sonic** (speech‑to‑speech) in real time.  
- **Processing:**  
  1. **Nova‑2‑Sonic** converts speech to text, then re‑generates a concise spoken summary every 2 minutes (so listeners hear a “live minutes” overlay).  
  2. Simultaneously, **Nova Multimodal Embeddings** index any shared slides/screenshots (uploaded via S3) and tag the transcript for “action‑item” detection.  
- **Delivery:** At meeting end, a single MP3 of the AI‑crafted summary and a searchable transcript (with slide thumbnails) are stored in an S3 bucket and emailed to attendees.  

### Why it fits  

| Requirement | How it’s met |
|-------------|--------------|
| **Core tech** | **Nova‑2‑Sonic** for speech‑to‑speech plus **Nova Multimodal Embeddings** for slide understanding. |
| **Scope** | End‑to‑end generative AI on AWS (Transcribe‑lite replacement, Lambda, S3, SES). |
| **Simplicity** | One streaming pipeline + one post‑processing job – no complex model‑training. |
| **Impact** | Saves hours of manual note‑taking for businesses, NGOs, remote teams (20 % impact). |
| **Technical depth** | Real‑time streaming, multimodal tagging, and audio synthesis showcase strong engineering (60 %). |
| **Creativity** | Live spoken summaries plus visual context linking is a fresh twist on meeting‑AI tools. |

---

## 3️⃣ Idea: **Snap‑Shop Assistant – Visual Product Search & Checkout Bot**  
**Category:** Multimodal Understanding + UI Automation (Nova‑Act)  

### Description  
- **User Flow:** On a mobile web page, a shopper snaps a photo of an item they own (e.g., a lamp).  
- **Engine:**  
  1. **Nova Multimodal Embeddings** encode the photo and compare it against a catalog of product images stored in a Pinecone‑style vector DB on Amazon OpenSearch.  
  2. The top‑5 matching products (title, price, rating) are shown instantly.  
  3. If the user clicks “Buy”, **Nova‑Act** drives a headless Chromium session (via AWS Lambda Container) that logs into the chosen e‑commerce site, adds the item to cart, and completes checkout using the user’s saved payment token (PCI‑compliant via AWS Payment Cryptography).  
- **Result:** One‑click purchase of visually‑matched items without manual search.  

### Why it fits  

| Requirement | How it’s met |
|-------------|--------------|
| **Core tech** | Leverages **Nova Multimodal Embeddings** for image similarity and **Nova‑Act** for automated UI checkout. |
| **Scope** | Full generative AI‑enhanced shopping assistant hosted on AWS (S3, Lambda, OpenSearch, DynamoDB). |
| **Simplicity** | Two main components (image‑search + checkout bot) keep the architecture straightforward. |
| **Impact** | Boosts accessibility for visually‑impaired shoppers and streamlines “photo‑to‑buy” for any retailer (20 % impact). |
| **Technical depth** | Shows high‑quality multimodal retrieval and secure agentic automation – strong technical scoring. |
| **Creativity** | Combines visual search with a fully automated purchase flow, a use‑case rarely seen in hackathons. |

---  

### Quick Demo Checklist (fits submission artefacts)

| Idea | Demo (< 3 min) | #AmazonNova tag | Repo access |
|------|----------------|-----------------|-------------|
| Nova‑Tutor | Walkthrough: prompt → syllabus → generated Notion page. | ✔️ | Public GitHub (or private with email access) |
| Voice‑Summarize | Live meeting capture → spoken summary snippet + final MP3. | ✔️ | Public GitHub |
| Snap‑Shop Assistant | Photo upload → matching products → automated checkout animation. | ✔️ | Public GitHub |

All three concepts satisfy the **mandatory Nova usage**, are **AWS‑native**, and balance **creativity**, **simplicity**, and **validity** to maximise the judging scores. Good luck! 🚀
