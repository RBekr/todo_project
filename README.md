# todo_project
TODO LIST

## Setup
```
$ git clone https://github.com/RBekr/api_yamdb.git
$ cd infra_sp2/infra
$ docker-compose up --build -d
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
$ docker-compose exec web python manage.py collectstatic --no-input
$ docker-compose exec web python manage.py loaddata fixtures.json
```