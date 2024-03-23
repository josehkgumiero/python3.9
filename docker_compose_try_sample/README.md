# Try Docker Compose

This tutorial is designed to introduce the key concepts of Docker Compose whilst building a simple Python web application. The application uses the Flask framework and maintains a hit counter in Redis.

# Prerequisits

You need to have Docker Engine and Docker Compose on your machine. 

# Define the application dependencies

- Create a directory for the project:
```
mkdir docker_compose_try_sample
cd docker_compose_try_sample
```

- Create a file called app.py:
```
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```

- Create another file called requirements.txt:
```
flask
redis
```

- In your project directory, create a file named Dockerfile:
```
# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

- Create a file called compose.yaml:
```
services:
  web:
    build: .
    ports:
      - "8000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_DEBUG: "true"
  redis:
    image: "redis:alpine"
```

- Start
```
docker compose up
```

# Reference

https://docs.docker.com/compose/gettingstarted/