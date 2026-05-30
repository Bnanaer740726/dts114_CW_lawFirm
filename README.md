# DTS114TC Coursework — AI-Powered Meta-Software Development

**2470669 · Weichu Zeng**

This repository supports the **Software Component** coursework: an AI-driven system that automatically generates SDLC artefacts and application code from a business problem, with version control, testing, and CI/CD for the generated output.

## Core deliverable: meta-software system

The primary artefact is **`Task1/meta_dev.ipynb`** — a Jupyter Notebook that implements the AI-DLC pipeline:

1. **Inception** — problem statement, personas, PRD, user stories  
2. **Construction** — UML diagrams, Flask REST API, HTML website (with AI-generated hero image)  
3. **Operations** — Docker packaging of the generated application  

Supporting module: `Task1/utils.py` (LLM client, PlantUML rendering, image generation).

**Business scenario:** law firm website (aligned with the presentation component).

The Flask site under `Task2/flask/` is an **example output** of the notebook, not the coursework subject itself.

## Repository layout

| Path | Purpose |
|------|---------|
| `Task1/meta_dev.ipynb` | Meta-software development pipeline (main submission) |
| `Task1/utils.py` | LLM and tooling helpers |
| `Task1/environment.yml` | Conda environment |
| `Task2/flask/` | Generated law firm application (sample output) |
| `Task2/tests/` | Pytest suite for the generated API |
| `Task2/screenshots/` | Evidence: commits, deployment, CI/CD |
| `.github/workflows/` | GitHub Actions pipeline |

## Engineering practices (generated application)

- **Stack:** Python 3.11, Flask  
- **Methodology:** AI-DLC with human oversight  
- **Pipeline:** build → test → Docker image verification on push to `main`

Requires a local `.env` with `APIFREE_API_KEY` when running the notebook (not committed to this repository).
