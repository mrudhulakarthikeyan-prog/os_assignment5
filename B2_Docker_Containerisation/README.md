# B2 – Containerise the Portal

## Flask application

The app is a small local assignment example. It provides `/`, `/health` and `/info`.
It is not a real student-results system and contains no student data.

## Build and run with Docker

From this folder:

```bash
docker build -t result-portal:assignment5 .
docker run -d --name result-portal -p 8000:8000 result-portal:assignment5
docker ps
curl http://localhost:8000
curl http://localhost:8000/health
docker images result-portal
docker exec result-portal whoami
docker stats --no-stream result-portal
docker history result-portal:assignment5
```

Expected runtime user: `portal`.

Stop and remove:

```bash
docker rm -f result-portal
```

## Compose with database

```bash
docker compose up --build -d
docker compose ps
docker compose logs
docker compose down
```

The Compose example includes a PostgreSQL service and a named persistent volume.
The sample Flask app does not yet query the database; the database service demonstrates
separate service deployment and persistent storage.

## Resource limits

```bash
docker run -d --name result-portal-limited -p 8001:8000 \
  --cpus="0.50" --memory="256m" result-portal:assignment5
docker stats --no-stream result-portal-limited
docker rm -f result-portal-limited
```

Save real outputs and image size in `outputs/`.
