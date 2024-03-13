# Flask

# User's Guideline

# Installation

- Flask supports Python 3.8 and newer;
- These distributions will be installed automatically:
    - Werkzeug
    - Jinja
    - MarkupSafe
    - ItsDangerous
    - Click
    - Blinker
- Optional dependencies:
    - python-dotenv
    - Watchdog
- You may choose to use gevent or eventlet, so greenlet >= 1.0 is required;

# Virtual Environments

- Manage the dependencies for the project, both in development and in production;
- Virtual Environments are independent groups of Python libraries, one for eac project;
```
mkdir myproject
cd myproject
python3 -m venv .venv
```
```
source .venv/bin/activate
```

# Install Flask

```
pip install Flask
```