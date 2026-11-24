FROM python:3.12-slim

# TODO 1 completed: set the application working directory.
WORKDIR /app

# Install dependencies before copying source to improve layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# TODO 2 completed: copy application source and create a non-root portal user.
RUN groupadd --system portal && useradd --system --gid portal --create-home portal
COPY --chown=portal:portal app/ /app/
USER portal

# TODO 3 completed: document port 8000 and launch Gunicorn on all container interfaces.
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
