import os
from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from gradient_adk import entrypoint, RequestContext
from gradient import AsyncGradient

import pathlib
import re
from pathvalidate import sanitize_filename

# --- 1. THE SHARED MEMORY (The 'State') ---
# This is where the agent stores and carries data through the workflow.
class HackathonState(TypedDict):
    raw_overview: str
    hackathon_name: str           
    requirements: List[str]
    judging_criteria: List[str]
    platform_accounts: List[dict]
    required_keys: List[str]
    
    gitignore_content: str
    requirements_content: str
    setup_commands: List[str]
    
    scaffold_files: List[str]
    project_concepts: List[str]

# --- 2. THE WORKSTATIONS (The 'Nodes') ---
# This function acts as your first workstation: The Analyst.
async def analyst_node(state: HackathonState):
    print("--- NODE 1: Analyzing Hackathon Overview ---")
    
    # Initialize the Gradient client using your secure access key
    inference_client = AsyncGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY")
    )

    # The System Prompt: Defines the "Expert Analyst" persona and specific rules
    system_instructions = (
        "You are a Senior Hackathon Analyst. Your goal is to extract structured setup data from a DEVPOST overview.\n"
        "RULES:\n"
        "1. Identify mandatory requirements (Must-Builds).\n"
        "2. Extract judging criteria and their importance.\n"
        "3. Identify proprietary platforms (e.g., DigitalOcean) that require account sign-ups.\n"
        "4. List specific API keys or access keys mentioned.\n"
        "FORMAT: Return your findings in a clear, categorized summary."
    )

    # Call the model (we use the 'openai-gpt-oss-120b' model provided by Gradient)
    response = await inference_client.chat.completions.create(
        model="openai-gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": f"Analyze this hackathon overview:\n\n{state['raw_overview']}"}
        ],
    )

    content = response.choices[0].message.content
    print(f"Analysis Complete: {content[:100]}...") # Log the first 100 chars for verification

    # In a production version, we would parse this content into the lists. 
    # For this hackathon step, we will store the raw analysis to be used by the Scaffolder.
    # Logic update: The LLM will now also identify the hackathon name.
    return {
        "hackathon_name": content.split('\n')[0].replace("#", "").strip(), # Grab first line as name
        "requirements": [content],
        "required_keys": ["GRADIENT_MODEL_ACCESS_KEY"]
    }

# This function acts as your second workstation: The Scaffolder.
async def scaffolder_node(state: HackathonState):
    print(f"--- NODE 2: Innovating Infrastructure for {state['hackathon_name'][:30]}... ---")
    
    # 1. Standardized Folder Naming
    # Force lowercase, remove special characters, and limit to a concise slug
    clean_name = re.sub(r'[^a-z0-9]+', '_', state['hackathon_name'].lower()).strip('_')
    folder_name = "_".join(clean_name.split('_')[:4]) 
    sandbox_path = pathlib.Path(f"./output/{folder_name}")
    sandbox_path.mkdir(parents=True, exist_ok=True)

    # Initialize the client for dual inference
    inference_client = AsyncGradient(model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY"))
    
    # 2. Dynamic Requirements Inference
    req_prompt = (
        f"Based on these requirements: {state['requirements'][0]}\n"
        "Return ONLY a comma-separated list of Python library names needed. "
        "Example: boto3, requests, pandas"
    )
    
    # 3. Dynamic Gitignore Inference
    gi_prompt = (
        f"Based on these requirements: {state['requirements'][0]}\n"
        "Return ONLY a comma-separated list of file patterns to ignore in Git. "
        "Example: .aws/, *.log, cdk.out/"
    )

    # Execution & Merging Logic
    async def get_inference(prompt):
        try:
            resp = await inference_client.chat.completions.create(
                model="openai-gpt-oss-120b",
                messages=[{"role": "user", "content": prompt}]
            )
            return [item.strip() for item in resp.choices[0].message.content.split(',') if item.strip()]
        except Exception as e:
            print(f"⚠️ Inference failed: {e}")
            return []

    # Get both sets of suggestions
    inferred_libs = await get_inference(req_prompt)
    inferred_ignores = await get_inference(gi_prompt)

    # Merge Strategy: Core Standard + LLM Inferred (Deduplicated)
    core_libs = ["gradient-adk", "gradient-sdk", "langgraph", "python-dotenv"]
    reqs_content = "\n".join(sorted(list(set(core_libs + [l.lower() for l in inferred_libs]))))

    core_ignores = [".env", ".venv/", "__pycache__/", "*.pyc", ".gradient/", ".DS_Store"]
    gitignore_content = "\n".join(sorted(list(set(core_ignores + inferred_ignores))))

    # 4. Physical Write to Sandbox
    (sandbox_path / ".gitignore").write_text(gitignore_content, encoding="utf-8")
    (sandbox_path / "requirements.txt").write_text(reqs_content, encoding="utf-8")

    print(f"✅ Sandbox created at: {sandbox_path}")

    return {
        "gitignore_content": gitignore_content,
        "requirements_content": reqs_content,
        "setup_commands": [
            f"cd ./output/{folder_name}",
            "python -m venv .venv",
            "pip install -r requirements.txt"
        ]
    }

# This function acts as your third workstation: The Creative.
async def creative_node(state: HackathonState):
    print("--- NODE 3: Brainstorming Project Concepts ---")
    
    # TRANSPARENCY: Verify we still have the data from Node 2
    has_gitignore = "YES" if "gitignore_content" in state else "NO"
    print(f"DEBUG: Creative Node received gitignore_content? {has_gitignore}")

    inference_client = AsyncGradient(
        model_access_key=os.environ.get("GRADIENT_MODEL_ACCESS_KEY")
    )

    # The Persona: Focused on your "Singles and Doubles" philosophy [cite: 11]
    system_instructions = (
        "You are a Creative Strategist for hackathons. Your goal is to brainstorm 2-3 project ideas.\n"
        "CRITERIA:\n"
        "1. Creative: Unique angles that stand out[cite: 36].\n"
        "2. Simple: Prioritize 'singles and doubles' over complex 'homeruns'.\n"
        "3. Valid: Must meet all extracted requirements[cite: 38].\n"
        "FORMAT: Return ideas with a Title, Description, and 'Why it fits' section."
    )

    response = await inference_client.chat.completions.create(
        model="openai-gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": f"Requirements: {state['requirements']}\n\nBrainstorm simple concepts."}
        ],
    )

    # Instead of state.update or state["key"] = ...
    # Just RETURN the new piece of data
    return {
        "project_concepts": [response.choices[0].message.content]
    }
    
# --- 3. THE ENTRYPOINT (DigitalOcean Integration) ---
# This is the 'Front Door' the platform uses to run your agent.
@entrypoint
async def main(input: dict, context: RequestContext):
    builder = StateGraph(HackathonState)
    builder.add_node("analyst", analyst_node)
    builder.add_node("scaffolder", scaffolder_node)
    builder.add_node("creative", creative_node)
    
    builder.add_edge(START, "analyst")
    builder.add_edge("analyst", "scaffolder")
    builder.add_edge("scaffolder", "creative")
    builder.add_edge("creative", END)
    
    graph = builder.compile()
    
    initial_input = {"raw_overview": input.get("text", "No overview provided.")}
    result = await graph.ainvoke(initial_input)

    # --- NEW: WRITE READABLE MARKDOWN REPORT ---
    with open("hackathon_report.md", "w", encoding="utf-8") as f:
        f.write("# 🏆 Hackathon Cold-Start Report\n\n")
        f.write("## 📋 1. Analysis & Requirements\n")
        f.write(f"{result['requirements'][0]}\n\n")
        
        f.write("## 🛠️ 2. Infrastructure Blueprint\n")
        f.write("### .gitignore Content:\n```text\n")

        # .get("key", "default") prevents the script from crashing if the key is missing
        f.write(f"{result.get('gitignore_content', 'Check Node 2 logs for content.')}\n```\n")
        f.write("### requirements.txt Content:\n```text\n")
        f.write(f"{result.get('requirements_content', 'Check Node 2 logs for content.')}\n```\n")
        
        f.write("## 🚀 3. Proposed Concepts (Singles & Doubles)\n")
        for concept in result['project_concepts']:
            f.write(f"{concept}\n")

    return result