# Automated User Cleanup System

## Project Overview

Django application with Celery background tasks for automated user cleanup, featuring a React TypeScript dashboard for monitoring and manual triggers.

## 1. Docker Setup

- **Docker Compose**: Multi-container setup (Django, PostgreSQL, Redis, Celery)
- **Environment Variables**: `.env` file for configuration
- **Build**: `docker compose up --build -d`
- **Access**: http://localhost:8000

## 2. Database & Models

- **PostgreSQL**: Database container
- **Django User Model**: Built-in authentication system
- **CleanupReport Model**: Tracks cleanup operations with timestamps and statistics
- **Migrations**: `docker exec -it django-docker python manage.py migrate`

## 3. Celery Background Tasks

- **Worker**: Processes cleanup tasks
- **Beat Scheduler**: Automated task scheduling
- **Redis**: Message broker and result backend
- **Task**: Deletes inactive users and logs cleanup reports

```bash
# Monitor Celery
docker logs -f celery-worker
docker logs -f celery-beat
```

## 4. RESTful API Endpoints

- **GET /api/reports/latest/**: Retrieve most recent cleanup report
- **POST /api/cleanup/trigger/**: Manually trigger cleanup task
- **Django REST Framework**: API serialization and views

## 5. React TypeScript Dashboard

### Frontend Structure

```
frontend/                 # Vite React development
├── src/
│   ├── App.jsx          # Main dashboard component
│   ├── App.css          # Styling
│   └── main.jsx         # Entry point
├── package.json         # Dependencies
└── dist/                # Build output
```

### Development Workflow

1. **Develop**: `cd frontend && npm run dev` (localhost:5173)
2. **Build**: `npm run build`
3. **Deploy**: Copy `dist/assets/` to Django static files

### Features

- **Data Fetching**: Connects to Django API endpoints
- **Table Display**: Shows cleanup reports with full-width styling
- **Manual Trigger**: Button to trigger immediate cleanup
- **Error Handling**: User-friendly error messages
- **Loading States**: Visual feedback during operations

## Key Commands

```bash
# Start services
docker compose up --build -d

# Database operations
docker exec -it code-avatar-db-1 psql -U dbuser -d dockerdjango

# Frontend development
cd frontend && npm run dev

# Production build
cd frontend && npm run build && cp -r dist/assets ../app/static/
```

## References

- [Django + Docker Tutorial](https://www.docker.com/blog/how-to-dockerize-django-app/)
- [Celery + Redis Implementation](https://www.youtube.com/watch?v=y6FG-kKhGwA)
- [Django REST Framework](https://www.youtube.com/watch?v=t-uAgI-AUxc)
