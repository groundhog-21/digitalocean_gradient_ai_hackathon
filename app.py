import os
import asyncio
import markdown2
from flask import Flask, render_template_string

# IMPORT: We bring in your existing logic without changing main.py
from gradient import AsyncGradient
from main import analyst_node, scaffolder_node, creative_node, HackathonState
from langgraph.graph import StateGraph, START, END

app = Flask(__name__)

# --- Re-build the Workflow for the Web Interface ---
def create_workflow():
    builder = StateGraph(HackathonState)
    builder.add_node("analyst", analyst_node)
    builder.add_node("scaffolder", scaffolder_node)
    builder.add_node("creative", creative_node)
    
    builder.add_edge(START, "analyst")
    builder.add_edge("analyst", "scaffolder")
    builder.add_edge("scaffolder", "creative")
    builder.add_edge("creative", END)
    
    return builder.compile()

@app.route('/')
async def run_agent_and_display():
    try:
        # NEW: Initialize the client locally for this request
        inference_client = AsyncGradient(
            model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY")
        )

        # 1. Load your local hackathon text
        input_file = "devpost_input.txt"
        if not os.path.exists(input_file):
            return f"<h1>Error</h1><p>Missing {input_file} in the root directory.</p>"
            
        with open(input_file, "r", encoding="utf-8") as f:
            hackathon_text = f.read()

        # 2. Run the existing agentic workflow logic
        graph = create_workflow()
        
        # UPDATED: Inject the client into the state
        initial_input = {
            "raw_overview": hackathon_text,
            "client": inference_client
        }
        result = await graph.ainvoke(initial_input)

        # --- Build the local reports ---
        import json
        
        # UPDATED: Save the JSON Report (Clean the client first)
        report_data = result.copy()
        if "client" in report_data:
            del report_data["client"]
            
        with open("hackathon_report.json", "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)
            
        # Save the Markdown Report
        local_md_content = f"""
# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
{result['requirements'][0]}

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
{result.get('gitignore_content', '')}
```

### requirements.txt Content:
```text
{result.get('requirements_content', '')}
```

## 🚀 3. Proposed Concepts
{result['project_concepts'][0]}
            """
        with open("hackathon_report.md", "w", encoding="utf-8") as f:
            f.write(local_md_content)

        # --- Build the web report ---
        report_md = f"""
# 🏆 Hackathon Cold-Start Report

## 📋 1. Analysis & Requirements
{result['requirements'][0]}

## 🛠️ 2. Infrastructure Blueprint
### .gitignore Content:
```text
{result.get('gitignore_content', 'Generated during run.')}
```

### requirements.txt Content:
```text
{result.get('requirements_content', 'Generated during run.')}
```

## 🚀 3. Proposed Concepts
{result['project_concepts'][0]}
            """
        
        # 4. Render directly to a professional Bootstrap webpage
        report_html = markdown2.markdown(report_md, extras=["fenced-code-blocks", "tables"])
        
        return render_template_string("""
            <!DOCTYPE html>
            <html>
                <head>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
                    <title>Live Agent Analysis</title>
                    <style>body { background:#f4f7f6; } .container { max-width: 900px; }</style>
                </head>
                <body class="py-5">
                    <div class="container bg-white shadow-lg p-5 rounded">
                        {{ content|safe }}
                    </div>
                </body>
            </html>
        """, content=report_html)
        
    except Exception as e:
        return f"<h1>Execution Error</h1><p>{str(e)}</p>", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)