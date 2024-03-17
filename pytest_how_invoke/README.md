# How to invoke pytest

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
echo .venv >> .gitignore
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

- Run tests in a module
```
pytest test_module.py
```

- Run tests in a directory
```
pytest testing/
```

- Run tests by keyword expressions:
```
pytest -k 'MyClass and not method'
```

- To run a specific test within a module:
```
pytest tests/test_mod.py::test_func
```

- To run all tests in a class:
```
pytest tests/test_mod.py::TestClass
```

- Specifying a specific test method:
```
pytest tests/test_mod.py::TestClass::test_method
```

- Specifying a specific parametrization of a test:
```
pytest tests/test_mod.py::test_func[x1,y2]
```

- Run tests by marker expressions
```
pytest -m slow
```

- Run tests from packages
```
pytest --pyargs pkg.testing
```

- Getting help on version, option names, environment variables
```
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
```

- To get a list of the slowest 10 test durations over 1.0s long:
```
pytest --durations=10 --durations-min=1.0
```

- You can early-load plugins (internal and external) explicitly in the command-line with the -p option:
```
pytest -p mypluginmodule
```

- To disable loading specific plugins at invocation time, use the -p option together with the prefix no:.
```
pytest -p no:doctest
```

- Calling pytest through python -m pytest
```
python -m pytest [...]
```

- Calling pytest from Python code
```
# content of myinvoke.py
import sys

import pytest


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
```

- Invoke the test of myinvoke.py file
```
pytest myinvoke.py
```