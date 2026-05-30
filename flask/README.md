# Law Firm Website — Flask Application

Flask REST API and HTML frontend for a law firm promotional site. The frontend includes an AI-generated hero banner and a feedback/inquiry form. Static assets are served by Flask on port 5005.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Open http://127.0.0.1:5005

## API Examples

### Health check

```bash
curl http://127.0.0.1:5005/health
```

### Submit client inquiry

```bash
curl -X POST http://127.0.0.1:5005/feedback \
  -H "Content-Type: application/json" \
  -d '{"name":"Jane Doe","email":"jane@example.com","message":"I need contract review.","type":"inquiry"}'
```

### List practice areas

```bash
curl http://127.0.0.1:5005/practice-areas
```

### List attorneys

```bash
curl http://127.0.0.1:5005/attorneys
```
