# Automated User Cleanup System

A Django application with Celery background tasks for automated user cleanup, featuring a React dashboard for monitoring and manual triggers.

## Features

- **Automated User Cleanup**: Two Celery tasks - `deactivate_inactive_users` (runs every minute, flags inactive users 30+ days) and `log_inactive_users` (runs every 5 minutes, deletes flagged users)
- **REST API**: Endpoints for cleanup reports and manual triggers
- **React Dashboard**: Real-time monitoring and manual cleanup controls
- **Docker Compose**: Complete containerized setup

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git

### First Time Setup

1. **Environment setup**

   ```bash
   # Copy environment template (create .env if not exists)
   cp .env.example .env  # or create .env with required variables
   ```

2. **Build and start services**

   ```bash
   docker compose up --build -d
   ```

3. **Run database migrations**

   ```bash
   docker exec -it django-docker python manage.py migrate
   ```

4. **Create superuser (optional)**

   ```bash
   docker exec -it django-docker python manage.py createsuperuser
   ```

5. **Access the application**
   - **Dashboard**: http://localhost:8000
   - **Admin**: http://localhost:8000/admin

## API Endpoints

- `GET /api/reports/latest/` - Get most recent cleanup report
- `POST /api/cleanup/trigger/` - Trigger manual cleanup

## Environment Variables

### see .env.example

Create a `.env` file with:

```env
DJANGO_SECRET_KEY="your-secret-key-here"
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,0.0.0.0
DATABASE_NAME=dockerdjango
DATABASE_USERNAME=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_HOST=db
DATABASE_PORT=5432
INACTIVITY_THRESHOLD_DAYS=30
```

## Services

- **Django Web**: http://localhost:8000
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
- **Celery Worker**: Background task processing
- **Celery Beat**: Task scheduling

## Development

### Monitor Services

```bash
docker logs -f celery-worker  # Celery worker logs
docker logs -f celery-beat    # Celery scheduler logs
docker logs -f django-docker  # Django logs
```

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Cache/Queue**: Redis
- **Task Queue**: Celery
- **Frontend**: React (Vite)
- **Containerization**: Docker Compose
