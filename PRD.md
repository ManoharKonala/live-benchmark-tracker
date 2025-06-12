# 📄 Product Requirements Document (PRD)

## 🧩 Project Title:
**Live Benchmark Tracker in README for IDEs, LLMs, and AI Agents**

## 🧠 Overview:
Build a GitHub repository that automatically updates live benchmark scores (performance, cost, latency, context length) for IDEs, LLMs, and AI Agents. The benchmark data will be displayed directly inside the `README.md`, updated daily using GitHub Actions and external data sources (APIs/scrapers).

## 🎯 Goals:
| Goal ID | Description |
| ------- | ------------------------------------------------------------------- |
| G1 | Provide an always up-to-date benchmark comparison of top tools in one place |
| G2 | Keep everything visible in the `README.md` for fast consumption and sharing |
| G3 | Automate data retrieval and formatting using GitHub Actions |
| G4 | Make the repository extensible — allow community contributions for more benchmarks |

## 🧱 Core Features:
| Feature ID | Name | Description |
| ---------- | ------------------------------- | ------------------------------------------------------------ |
| F1 | Auto-Updated README Table | Table in `README.md` showing latest benchmark scores |
| F2 | GitHub Actions Workflow | Scheduled GitHub Action (e.g., every 6 hours) triggers the update script |
| F3 | Data Scraping / API Integration | Scripts to fetch benchmark data from public sources like HuggingFace, LMSYS, PapersWithCode |
| F4 | Scripted README Rewriting | Script replaces old benchmark section with fresh Markdown |
| F5 | Timestamp Display | Shows “Last updated: YYYY-MM-DD HH:MM UTC” |
| F6 | Optional: Chart Rendering | (Future) Generates charts as images and includes them in the README |
| F7 | Config File | `benchmark_config.yaml` defines which models/tools to track |
| F8 | Manual Trigger | Allow workflow_dispatch for manual update runs |

## 🛠️ Tech Stack:
| Component | Tool/Language |
| --------- | ------------- |
| Backend Script | Python (requests, BeautifulSoup, Pandas) |
| Automation | GitHub Actions |
| Data Storage | In-memory (JSON/CSV); no database required |
| Visualization | Markdown tables (README), optional PNG charts |
| Version Control | GitHub |
| Optional (future) | Matplotlib / Seaborn / Chart.js (for charts) |

## 📁 Folder Structure
```
/live-benchmark-tracker
├── /scrapers
│   ├── llm_scraper.py
│   ├── ide_scraper.py
│   └── agent_scraper.py
├── /data
│   └── benchmark.json
├── /utils
│   └── formatter.py
├── update_readme.py
├── benchmark_config.yaml
├── README.md
└── .github/workflows/update_readme.yml
```

## 🔁 Workflow Diagram
```mermaid
flowchart TD
    A[GitHub Action Triggered (Scheduled)] --> B[Run Python Script]
    B --> C[Fetch Benchmarks from APIs / Scrapers]
    C --> D[Format Markdown Table]
    D --> E[Replace Section in README.md]
    E --> F[Commit & Push Changes]
```

## ⏱️ Schedule
| Task | ETA |
| ------------------------------- | ------- |
| Initial repo + README + config | Day 1 |
| Add LLM benchmark script | Day 2 |
| Add GitHub Action for auto-update | Day 3 |
| Add IDE & Agent data sources | Day 4–5 |
| Final polish, visuals, badges | Day 6 |

## 🔍 External Data Sources
| Category | Source | Integration Method |
| -------- | ------------------------------- | ------------------- |
| LLMs | HuggingFace Open LLM Leaderboard | API / scrape |
| LLMs | LMSYS Chatbot Arena | Scrape HTML |
| IDEs | JetBrains, VS Code CI logs | Scrape/Parse GitHub |
| AI Agents | SWE-bench, AutoEval | GitHub parsing |

## 📈 Sample Output in README.md
```markdown
## 🔥 Live Benchmarks (Updated Daily)
| Tool/Model     | MMLU (%) | HumanEval (%) | Context Length | Cost ($/1k tokens) |
|----------------|----------|----------------|----------------|--------------------|
| GPT-4-turbo    | 86.5     | 83.0           | 128k           | $0.01              |
| Claude 3 Opus  | 89.1     | 87.5           | 200k           | $0.01              |
| Gemini 1.5 Pro | 87.0     | 86.0           | 1M (streaming) | $0.005             |
| VS Code        | --       | --             | --             | 450ms startup time |
🕒 _Last updated: 2025-06-12 08:00 UTC_
```

## 🧩 Future Enhancements
| Feature | Description |
| ------------------------------ | -------------------------------- |
| Interactive Charts | Visual trendline of benchmark changes over time |
| LLM Accuracy Over Time | Auto-plot chart of model performance |
| Community Plugin Submissions | Allow users to submit PRs to benchmark new tools |
| Integration with HuggingFace Spaces | Live dashboard web app version |

## 🛡️ Risks and Mitigations
| Risk | Mitigation |
| ----------------------- | ------------------------------------- |
| API limits / site blocks | Use caching and low-frequency polling |
| HTML structure changes | Modular scraping with fallback |
| Large README size | Limit table rows to top 5–10 items |
| Inconsistent metrics | Normalize units in Python scripts |

## 📌 Success Criteria
* [ ] README updates automatically with no manual work
* [ ] Shows accurate, reliable data from live sources
* [ ] Easy to extend with new models/tools
* [ ] Gets visibility (stars, forks) from the open-source community
