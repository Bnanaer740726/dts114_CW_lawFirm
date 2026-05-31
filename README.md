# DTS114TC Coursework — AI-Powered Meta-Software Development

**2470669 · Weichu Zeng**

An AI-driven system that automatically generates artefacts and application code from a business problem, with version control, testing, and CI/CD for the generated output.

## Core deliverable

**`meta-system/meta_dev.ipynb`** — Jupyter Notebook implementing the AI-DLC pipeline:

1. **Inception** — problem statement, personas, PRD, user stories  
2. **Construction** — UML diagrams, Flask REST API, HTML website (with AI-generated hero image)  
3. **Operations** — Docker packaging of the generated application  

Supporting module: `meta-system/utils.py` (LLM client, PlantUML rendering, image generation).

**Business scenario:** law firm website (aligned with the presentation component).

The Flask site under `deployment/flask/` is **example output** from the notebook.

## Repository layout

| Path | Purpose |
|------|---------|
| `meta-system/meta_dev.ipynb` | Meta-software development pipeline |
| `meta-system/utils.py` | LLM and tooling helpers |
| `meta-system/environment.yml` | Conda environment |
| `deployment/flask/` | Generated law firm application |
| `deployment/tests/` | Pytest suite for the generated API |
| `deployment/screenshots/` | Evidence: commits, deployment, CI/CD |
| `.github/workflows/` | GitHub Actions pipeline |

## Engineering practices

- **Stack:** Python 3.11, Flask  
- **Methodology:** AI-DLC with human oversight  
- **Pipeline:** build → test → Docker image verification on push to `main`

Requires a local `.env` with `APIFREE_API_KEY` when running the notebook (not committed to this repository).
