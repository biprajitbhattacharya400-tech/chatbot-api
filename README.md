# Chatbot API

FastAPI backend with CRUD routes, Groq-backed AI endpoints, semantic document search, and a LangChain agent.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Set `GROQ_API_KEY` in `.env`, then run:

```powershell
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Health check:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/health
```

## Deploying on Render

This repo is configured for a Render web service.

- Build command: `pip install --no-cache-dir -r requirements.txt`
- Start command: `python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}`
- Python version: `3.11.9` via `.python-version`
- Required env var: `GROQ_API_KEY`
- Optional env vars: `GROQ_MODEL`, `DATABASE_URL`

Important:

- The API now starts without loading embeddings or the LangChain agent during import, so Render can detect the open port quickly.
- If `DATABASE_URL` is not set, the app uses local SQLite at `users.db`.
- Render local disk is ephemeral. If you want persistent user data, set `DATABASE_URL` to Postgres or another hosted database instead of SQLite.

## Endpoints

- `GET /`
- `GET /health`
- `GET /users`
- `GET /users/top`
- `POST /users/`
- `POST /ask-ai`
- `POST /ask-doc`
- `POST /agent`
