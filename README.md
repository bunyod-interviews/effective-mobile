# Effective Mobile

DevOps test project: Python HTTP backend behind nginx reverse proxy, orchestrated with Docker Compose.

**Stack:** Python, nginx, Docker, Docker Compose.

## Architecture

```
curl :80 → [proxy / nginx] → [backend :8080]
              ↑ host              ↑ docker network only
```

Nginx accepts HTTP on port 80 and proxies `/` to the `backend` service. The backend port is exposed only inside the Docker network, not on the host.

## Quick start

**Prerequisites:** Docker and Docker Compose.

```bash
cp .env.example .env    # set PORT=8080
docker compose up --build
curl http://localhost   # → Hello from Effective Mobile!
docker compose down
```

`PORT` must stay in sync across `.env`, `nginx/nginx.conf`, `docker-compose.yml`, and `backend/Dockerfile` — see comments in `.env.example`. For the default setup (`8080`), only `.env` needs editing.

## Project structure

```
├── backend/          (Dockerfile, app.py)
├── nginx/            (nginx.conf)
├── docker-compose.yml
├── .env.example
└── README.md
```
