# Application Flask Quickstart
```
mkdir application_flask_quickstart
cd application_flask_quickstart
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install Flask
```
# Debug Mode
```
python3 -m flask run --debug
```
# Externally Visible Server
```
python3 -m flask run --host=0.0.0.0
```
```
http://localhost:5000/
```
```
http://127.0.0.1:5000/
```