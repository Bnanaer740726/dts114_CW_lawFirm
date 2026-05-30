# Task 2 — Version Control, CI/CD, and Deployment

## Prerequisites

1. Run `Outputs/Task1/meta_dev.ipynb` to generate the Flask app under `artifacts/app/flask/`.
2. Copy generated files into this folder:

```powershell
Copy-Item -Recurse -Force Outputs\Task1\artifacts\app\flask Task2\flask
```

## Local run

```powershell
cd flask
pip install -r requirements.txt
python main.py
```

Open http://127.0.0.1:5005 — the page should show the AI-generated hero image.

## Docker

From `Task2/`:

```powershell
docker-compose up --build
```

## Git & GitHub

```powershell
git init
git add .
git commit -m "feat: law firm meta-software with CI/CD"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/law-firm-cw.git
git push -u origin main
```

**Screenshot 1:** GitHub commit history or `git log --oneline`.

## CI/CD (GitHub Actions)

Workflow file: `.github/workflows/ci-cd.yml`

- **Build:** install Python dependencies
- **Test:** run `pytest` against `/health` and `/feedback`
- **Docker build:** verify the container image builds on `main`

**Screenshot 3:** GitHub Actions tab showing a green workflow run.

## Deployment (Render — recommended)

1. Create a free account at https://render.com
2. New → Web Service → connect your GitHub repo
3. Settings:
   - **Root Directory:** `Task2` (or repo root if Task2 is the repo)
   - **Build Command:** `pip install -r flask/requirements.txt`
   - **Start Command:** `cd flask && python main.py`
   - **Port:** 5005
4. Deploy and open the public URL.

**Screenshot 2:** Browser showing the deployed law firm website with the hero image.

## Screenshots folder

Save the three required screenshots under `screenshots/`:

- `commits.png`
- `deployment.png`
- `cicd_workflow.png`
