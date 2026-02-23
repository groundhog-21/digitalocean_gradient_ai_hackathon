# Hackathon Helper

**Hackathon Helper** is an AI-powered orchestration tool designed to eliminate the "cold-start" problem of hackathons. By automating the transition from a dense Devpost overview to a structured technical blueprint, it ensures developers spend their first hour coding instead of configuring.

## 🌟 Core Philosophy: Strategic Delivery
Success in a hackathon is about consistency and reliability. This tool is built to help you meet every requirement and ship a functional, polished project by identifying a clear, achievable path through the requirements from the very start.

---

## 🚀 Features
* **Strategic Analysis:** Extracts mandatory requirements and proprietary platform constraints (like DigitalOcean or GitLab integrations).
* **Dynamic Scaffolding:** Automatically generates `.gitignore` and `requirements.txt` based on the AI's prediction of your project's specific library needs.
* **Creative Brainstorming:** Suggests achievable project concepts tailored to the extracted hackathon criteria.
* **Professional Dashboard:** A Flask-based web interface (`app.py`) that renders your blueprint into a polished, browser-based report for high-quality presentation.

---

## 📂 Project Structure
The project is organized to support both the multi-agent logic and the professional presentation layer:

```text
DIGITALOCEAN_GRADIENT_AI_HACKATHON
├── app.py                # Flask Web Interface (Professional Reporting)
├── main.py               # Core Multi-Agent Logic (LangGraph + Gradient)
├── devpost_input.txt     # The "Source of Truth" (Paste Hackathon text here)
├── hackathon_report.md   # Markdown Output
├── hackathon_report.json # Data Output
├── output/               # Generated Project Sandboxes
└── docs/                 # Documentation & Logs
```

---

## 🛠️ How It Works
The system uses a LangGraph multi-agent workflow powered by Gradient AI:

1. **Analyst Node:** Maps out the mandatory "Must-Builds" and technical constraints.

2. **Scaffolder Node:** Reasons about Python dependencies and creates the local environment files.

3. **Creative Node:** Identifies valid, high-potential ideas that fit the specific hackathon scope.

4. **Flask Layer (`app.py`):** Dynamically executes the workflow and renders the results in a clean, professional dashboard.

---

## ⚡ Quick Start

### 1. Setup Environment
Ensure your `.env` file contains your `DIGITALOCEAN_API_TOKEN` and `GRADIENT_MODEL_ACCESS_KEY`.
```bash
pip install -r requirements.txt
```

### 2. Add Your Hackathon
Paste the text from the hackathon overview page on [DEVPOST](https://devpost.com/) into devpost_input.txt.

### 3. Run the Helper & Initialize Project
Launch the web dashboard. This single command triggers the multi-agent workflow, generates your project scaffolding, and prepares your report:

```bash
python app.py
```

### 4. Results & Scaffolding
* **Browser Report:** Navigate to **http://localhost:8081** to view the professionally rendered analysis and project concepts.
* **Physical Scaffolding:** Check the `/output/` directory. The agent will have automatically created a new folder named after the hackathon containing your customized `.gitignore` and `requirements.txt`.
* **Data Exports:** Find the raw `hackathon_report.json` and `hackathon_report.md` in the root directory for your records.

---

## 🎓 What We Learned
Building this tool demonstrated the power of Multi-Agent Systems (MAS). By breaking down the problem into specialized roles (Analyst, Scaffolder, Creative), we achieved much higher accuracy and utility than a single LLM prompt could provide.

## 🔭 What's Next
**GitLab Integration:** Auto-committing scaffolded files to a new repository via webhooks.

**Cloud Deployment:** Migrating the local dashboard to a persistent cloud environment.

**Multi-Language Support:** Expanding scaffolding beyond Python to include Node.js, Rust, and Go.

---

_Built for the DigitalOcean & Gradient AI Hackathon._

