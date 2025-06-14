import os
import json
import sys # Import sys
import requests
from datetime import datetime
from utils.formatter import format_markdown_table
from scrapers.llm_scraper import fetch_llm_benchmarks
from scrapers.ide_scraper import fetch_ide_benchmarks
from scrapers.agent_scraper import fetch_agent_benchmarks

DATA_PATH = 'data/benchmark.json'
README_PATH = 'README.md'

if not os.path.exists('data'):
    os.makedirs('data')

def main():
    llm_data, ide_data, agent_data = [], [], [] # Initialize here
    try:
        # Fetch data
        print("Fetching LLM benchmarks...")
        llm_data = fetch_llm_benchmarks()
        print("Fetching IDE benchmarks...")
        ide_data = fetch_ide_benchmarks()
        print("Fetching Agent benchmarks...")
        agent_data = fetch_agent_benchmarks()
        print("All data fetched successfully.")
    except Exception as e:
        print(f"ERROR: Failed to fetch benchmark data. Details: {e}")
        sys.exit(1)

    # Combine
    print("Combining data...")
    all_data = llm_data + ide_data + agent_data

    # Save
    with open(DATA_PATH, 'w') as f:
        json.dump(all_data, f, indent=2)

    # Format table
    table_md = format_markdown_table(all_data)

    # Update README
    with open(README_PATH, 'r') as f:
        readme = f.read()
    new_section = f"""## 🔥 Live Benchmarks (Updated Daily)\n\n{table_md}\n\n🕒 _Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}_\n"""
    import re
    readme = re.sub(r'## 🔥 Live Benchmarks \(Updated Daily\)[\s\S]*?🕒 _Last updated:.*?_', new_section, readme, flags=re.MULTILINE)
    with open(README_PATH, 'w') as f:
        f.write(readme)

if __name__ == '__main__':
    main()
