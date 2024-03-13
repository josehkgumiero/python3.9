# Application Flask Quickstart
# Create Virtual Environment
```
mkdir application_flask_quickstart
cd application_flask_quickstart
python3 -m venv .venv
```
# Start Virtual Environment
```
source .venv/bin/activate
```
# Install Flask
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
# Request to localhost
```
http://localhost:5000/
```
# Request to Endpoint
```
http://127.0.0.1:5000/
```