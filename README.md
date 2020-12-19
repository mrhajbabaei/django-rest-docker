# Django REST Docker

REST API design with Django and Docker together.

## Steps:

1- Base App
docker-compose run app (service name on docker-compose.yml file) sh -c "django-admin.py startproject app (application name) . (current directory: WORKDIR on Dockerfile)"

2- Core App (our api and database management)
docker-compose run app sh -c "python manage.py startapp core"
