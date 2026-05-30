# DTS114TC Coursework — Task 2

**2470669 · Weichu Zeng**

Law firm website and Flask API, generated via the Task 1 meta-software pipeline and deployed under version control with CI/CD.

## Scope

Task 2 covers deployment and engineering practices for the application produced in Task 1: a promotional site for a law firm (team profiles, client inquiries, AI-generated hero image) backed by a REST API.

## Contents

| Path | Role |
|------|------|
| `flask/` | Application source (`main.py`, `index.html`, `images/hero.png`) |
| `tests/` | Unit tests (pytest) |
| `.github/workflows/` | GitHub Actions pipeline |
| `docker/` | Container configuration |
| `screenshots/` | Coursework evidence (commits, deployment, CI/CD) |

## Technical Summary

- **Stack:** Python 3.11, Flask, flask-cors  
- **Port:** 5005  
- **Methodology:** AI-DLC with human oversight  
- **Pipeline:** build → test → Docker image verification on push to `main`

## API (summary)

`GET /health` · `GET /practice-areas` · `GET /attorneys` · `POST /feedback` · `GET /feedback/<id>`

Entry point: `flask/main.py`
