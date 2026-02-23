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
        # 4. Render directly with sophisticated custom CSS
        report_html = markdown2.markdown(report_md, extras=["fenced-code-blocks", "tables"])
        
        return render_template_string("""
            <!DOCTYPE html>
            <html>
                <head>
                    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
                    <title>Hackathon Intelligence Report</title>
                    <style>
                        body { 
                            background: #fdfdfd; 
                            font-family: 'Inter', -apple-system, sans-serif; 
                            color: #2d3436; 
                            line-height: 1.5;
                        }
                        .container { 
                            max-width: 820px; 
                            margin-top: 4rem; 
                            margin-bottom: 4rem;
                            border: 1px solid #eaeaea;
                        }
                        
                        /* Header Scaling - Clean & Compact */
                        h1 { font-size: 1.6rem; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 1.5rem; color: #111; }
                        h2 { font-size: 1.25rem; font-weight: 600; margin-top: 2rem; color: #444; border-bottom: 1px solid #f0f0f0; padding-bottom: 8px; }
                        h3 { font-size: 1.05rem; font-weight: 600; color: #555; }
                        
                        /* Body Text Refinement */
                        p, li, td { font-size: 0.92rem; color: #444; }
                        
                        /* Fix for Numbering Scale */
                        ol { padding-left: 1.2rem; }
                        ol li::marker { 
                            font-weight: 600; 
                            font-size: 0.95rem; 
                            color: #000;
                        }
                        
                        /* Table Polish */
                        table { margin: 1.5rem 0; width: 100%; }
                        th { background: #f8f9fa; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; }
                        td { vertical-align: top; border-bottom: 1px solid #f1f1f1; }

                        /* Code blocks for Blueprint section */
                        pre { background: #f4f4f4; border-radius: 6px; padding: 1rem; font-size: 0.85rem; border: 1px solid #eee; }
                    </style>
                </head>
                <body class="py-2">
                    <div class="container bg-white shadow-sm p-5 rounded-3">
                        {{ content|safe }}
                    </div>
                </body>
            </html>
        """, content=report_html)
 
    except Exception as e:
        return f"<h1>Execution Error</h1><p>{str(e)}</p>", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)