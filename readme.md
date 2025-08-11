# AUTOMATED USER CLEANUP

1. Setting up Docker

- Docker-compose and Dockerfile
- Setting up .env files for variables
- setting up requirements.txt for all of the packages
- Build Django appilication "docker compose run django-web django-admin startproject <app_name> . "
  Source : https://forums.docker.com/t/connect-from-django-app-in-a-docker-container-to-redis-in-another-docker-container/143781

  https://www.docker.com/blog/how-to-dockerize-django-app/

2. Run Docker container and Django server, run migration

- docker compose up --build -d (runs on localhost:8000 (port))

  2.1 - docker exec -it django-docker python manage.py migrate - Run migrations
  2.2 - Creating super user : docker exec -it django-docker python manage.py createsuperuser

3. Postgres container
   psql -U dbuser -d dockerdjango

4. Use the existing admin user model available in Django

5. Create models.py to add the cleanup model

- add the cleanup model in admin.py

6. Automate with Celery

## Experiment with celery : see the logs

<code>docker exec -it django-docker celery -A automated_user_cleanup worker --loglevel=info </code>

- Redis instance with docker compose

## Dummy data creation and dump to database

docker cp dummy_data/auth_user_inserts.sql code-avatar-db-1:/auth_user_inserts.sql

docker exec -it code-avatar-db-1 bash

psql -U dbuser -d dockerdjango -f /auth_user_inserts.sql

## added celery-beat for scheduling tasks

`docker logs -f celery-worker` - logs celery-worker
`docker logs -f celery-beat` - logs celery-beat
