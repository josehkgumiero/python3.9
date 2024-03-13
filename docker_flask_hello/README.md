# Python Docker Flask Hello App
- This project is sample popular flask framework application hello world;
- Prerequisites
    - Docker Desktop installed;
    - git client;
- Initialize Docker assets: ``docker init``
```
docker init
Welcome to the Docker Init CLI!

This utility will walk you through creating the following files with sensible defaults for your project:
  - .dockerignore
  - Dockerfile
  - compose.yaml
  - README.Docker.md

Let's get started!

? What application platform does your project use? Python
? What version of Python do you want to use? 3.10.12
? What port do you want your app to listen on? 8000
? What is the command to run your app? python3 -m flask run --host=0.0.0.0
```
- Write the requirements.txt file:
```
blinker==1.6.2
click==8.1.6
colorama==0.4.6
Flask==2.3.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
Werkzeug==2.3.6
```
- Write the .flaskenv file:
```
FLASK_ENV=development
FLASK_APP=app.py
```
- Run the application: ``docker compose up --build``
- Open he browser: ``http://localhost:8000``
- Stop the docker: ```docker compose down```