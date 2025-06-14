import requests

def fetch_ide_benchmarks():
    # Example: Fetch VS Code CI build times from GitHub Actions API (public repo)
    url = "https://api.github.com/repos/microsoft/vscode/actions/runs?per_page=1"
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        runs = data.get("workflow_runs", [])
        if runs:
            latest = runs[0]
            duration = (latest["updated_at"] if latest.get("updated_at") else "--")
            return [{
                "Tool/Model": "VS Code",
                "MMLU (%)": "--",
                "HumanEval (%)": "--",
                "Context Length": "--",
                "Cost ($/1k tokens)": f"Build finished: {duration}"
            }]
        else:
            return [{
                "Tool/Model": "VS Code",
                "MMLU (%)": "--",
                "HumanEval (%)": "--",
                "Context Length": "--",
                "Cost ($/1k tokens)": "No recent build info"
            }]
    except Exception as e:
        raise
