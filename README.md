# FastAPI Coffee Shop ☕

A small learning project for understanding how APIs work in a real product flow.

## What you can learn
- Build API endpoints with FastAPI.
- Connect API + database (SQLite via SQLModel).
- Render web pages (Jinja templates).
- Use one app for two roles:
  - Customer page to create orders.
  - Kitchen dashboard to update status and monitor stock.

## Features
- Customer ordering website (`/`)
- Kitchen dashboard (`/kitchen`)
- Inventory system with stock validation
- Order status workflow (`RECEIVED`, `PREPARING`, `READY`, `CANCELLED`)
- Auto API docs (`/docs`)

## Run locally
```bash
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

## Open in browser
- Customer page: http://127.0.0.1:8000/
- Kitchen page: http://127.0.0.1:8000/kitchen
- API docs: http://127.0.0.1:8000/docs

## Learning lessons
- Step-by-step guide: `docs/lessons.md`

---

## How to host this project

### Option A: Render (easiest for beginners)
1. Push this repo to GitHub.
2. Create a new **Web Service** in Render and connect your repo.
3. Use these settings:
   - **Runtime**: Python
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
4. Deploy.
5. Open your Render URL (for example `https://your-app.onrender.com`).

> Note: this project uses SQLite (`coffee.db`). On many cloud platforms, local disk can be ephemeral, so data may reset on restart/redeploy.

### Option B: VPS (Ubuntu + systemd + Nginx)
1. Install Python and dependencies on server.
2. Clone project and install requirements.
3. Run app with Uvicorn bound to localhost:
   ```bash
   uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
   ```
4. Put Nginx in front as reverse proxy to `127.0.0.1:8000`.
5. Add HTTPS using Let's Encrypt (`certbot`).
6. Use `systemd` to keep app running on reboot.

### Option C: Docker-based hosting
If you want, I can also generate `Dockerfile` + `docker-compose.yml` so you can host with one command on any VM.

## Production note
For real production usage, move database from SQLite to PostgreSQL and use managed DB hosting.
