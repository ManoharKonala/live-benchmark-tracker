import requests

def fetch_agent_benchmarks():
    # Example: Fetch SWE-bench leaderboard from GitHub raw JSON
    url = "https://raw.githubusercontent.com/princeton-nlp/SWE-bench/main/leaderboard/leaderboard.json"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        results = []
        for entry in data.get("leaderboard", []):
            results.append({
                "Tool/Model": entry.get("model", ""),
                "MMLU (%)": entry.get("mmlu", "--"),
                "HumanEval (%)": entry.get("humaneval", "--"),
                "Context Length": entry.get("context_length", "--"),
                "Cost ($/1k tokens)": entry.get("cost", "--")
            })
        return results
    except Exception as e:
        print(f"Error fetching agent benchmarks: {e}")
        return []
