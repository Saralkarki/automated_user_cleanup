# AUTOMATED USER CLEANUP

1. Setting up Docker

- Docker-compose and Dockerfile
- Setting up .env files for variables
- setting up requirements.txt for all of the packages
- Build Django appilication "docker compose run django-web django-admin startproject <app_name> . "

2. Run Docker container and Django server, run migration

- docker compose up --build -d (runs on localhost:8000 (port))

  2.1 - docker exec -it django-docker python manage.py migrate - Run migrations
  2.2 - Creating super user : docker exec -it django-docker python manage.py createsuperuser

3. Postgres container
   psql -U dbuser -d dockerdjango

4. Editing the admin model available in the django.contrib.auth.model
