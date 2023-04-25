
FROM python:3.7-slim

WORKDIR /app

COPY todo/requirements.txt .


RUN pip3 install -r requirements.txt --no-cache-dir

COPY todo/ .


CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 