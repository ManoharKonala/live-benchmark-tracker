import requests

def fetch_llm_benchmarks():
    url = "https://huggingface.co/api/leaderboards/open-llm"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        results = []
        for model in data.get("models", []):
            results.append({
                "Tool/Model": model.get("model_name", ""),
                "MMLU (%)": model.get("mmlu", ""),
                "HumanEval (%)": model.get("humaneval", ""),
                "Context Length": model.get("context_length", ""),
                "Cost ($/1k tokens)": model.get("cost", "")
            })
        return results
    except Exception as e:
        print(f"Error fetching LLM benchmarks: {e}")
        return []
