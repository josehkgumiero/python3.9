# How to invoke pytest

- Entenr the project directory:
```
cd pytest_how_write_report_assertion
```

- Displays wether the pytest package has been installed:
```
py -m pip show pytest
```

- All the command-line flags can be obtained by running:
```
pytest --help
```

- Starts the virtual environment:
```
python -m venv .venv
```

- Writes the created virtual environment folder (.venv) to the gitignore file:
```
echo *.venv/ >> .gitignore
```

- To activate the virtual environment folder (.venv):
```
.venv\Scripts\activate.bat
```

- Lists the packages installed in the virtual environment (.venv)
```
py -m pip list
```

- Installs the pytest package:
```
pip install -U pytest
```

- Displays wether the pytest package has been installed:
```
py -m pip show pytest
```

