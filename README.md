<<<<<<< HEAD

# Todo project
TODO LIST - Классическое MVT web приложения, позволяющее создавать, редактировать и удалять задачи. 

_Используемые Технологии_
* Django==2.2.16
* Python 3
* CSS
* HTML

## Setup
```
$ git clone https://github.com/RBekr/todo_project.git
$ cd todo_project/infra
$ docker-compose up --build -d
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
$ docker-compose exec web python manage.py collectstatic --no-input
$ docker-compose exec web python manage.py loaddata fixtures.json
```
