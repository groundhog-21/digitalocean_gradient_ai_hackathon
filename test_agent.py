import requests

# This matches the local URL your 'gradient agent run' command is hosting
url = "http://localhost:8080/run"

# The data we want to send to our agent
data = {
    "prompt": "Hello! Confirm if you can access the Gradient models."
}

print("Sending request to local agent...")

try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("✅ Success!")
        print("Agent Response:", response.json())
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"❌ Connection failed: {e}")