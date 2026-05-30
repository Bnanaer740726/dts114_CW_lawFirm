# Flask Feedback API + HTML Frontend

An integrated Flask app that provides a simple Feedback API and an interactive HTML frontend for submitting and viewing feedback. The frontend is served automatically by Flask¡ªno separate static server or build step required.

## Setup

```bash
pip install flask flask-cors
```

## Run

```bash
python main.py
```

## Access

Open the app in your browser:

- http://127.0.0.1:5005

The interactive HTML UI loads from the same server and can be used to submit feedback and view stored entries.

## API Usage (cURL)

### POST `/feedback` (submit feedback)

```bash
curl -X POST http://127.0.0.1:5005/feedback \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex","message":"Great app!","rating":5}'
```

### GET `/feedback` (list feedback)

```bash
curl http://127.0.0.1:5005/feedback
```