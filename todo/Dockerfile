
FROM python:3.7-slim

WORKDIR /app

COPY todo/requirements.txt .


RUN pip3 install -r requirements.txt --no-cache-dir

COPY todo/ .


CMD ["gunicorn", "todo.wsgi:application", "--bind", "0:8000" ] 