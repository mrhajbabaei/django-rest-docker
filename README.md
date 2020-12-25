# Django REST Docker

REST API design with Django and Docker together.

## Steps:

1- Base App

docker-compose run app (service name on docker-compose.yml file) sh -c "django-admin.py startproject app (application name) . (current directory: WORKDIR on Dockerfile)"

2- Core App (our api and database management)

docker-compose run app sh -c "python manage.py startapp core"

3- \*\*Destruction container completely and make it again from scratch:

sudo docker-compose up --force-recreate --build --remove-orphans --always-recreate-deps --renew-anon-volumes

4- Create an endpoint to manage users:

docker-compose run --rm app sh -c "python manage.py startapp user"
\*\* --rm: remove docker container before making new one (it's not necessary)
