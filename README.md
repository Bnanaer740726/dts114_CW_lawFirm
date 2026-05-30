# DTS114TC Coursework — Law Firm Website

**2470669 · Weichu Zeng**

Deployment repository for an AI-generated law firm website and Flask API, including version control, automated testing, and CI/CD.

## Scope

This project implements the **Software Component (deployment)** of the coursework: a promotional site for a law firm (team profiles, client inquiries, AI-generated hero image) backed by a REST API. The meta-software pipeline that generates the application is submitted separately as a Jupyter Notebook.

## Contents

| Path | Role |
|------|------|
| `flask/` | Application source (`main.py`, `index.html`, `images/hero.png`) |
| `tests/` | Unit tests (pytest) |
| `.github/workflows/` | GitHub Actions pipeline |
| `docker/` | Container configuration |
| `screenshots/` | Evidence: commits, deployment, CI/CD workflow |

## Technical Summary

- **Stack:** Python 3.11, Flask, flask-cors  
- **Port:** 5005  
- **Methodology:** AI-DLC with human oversight  
- **Pipeline:** build → test → Docker image verification on push to `main`

## API (summary)

`GET /health` · `GET /practice-areas` · `GET /attorneys` · `POST /feedback` · `GET /feedback/<id>`

Entry point: `flask/main.py`
