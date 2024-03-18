# Reduce dataset size

- Creates the project directory:
```
mkdir reduce_dataset_size
```

- Entenr the project directory:
```
cd reduce_dataset_size
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

# Install new local python packages

- Lists the packages installed in the virtual environment (.venv)
```
py -m pip list
```

- Installs the pandas package:
```
py -m pip install pandas
```

- Displays wether the pandas package has been installed:
```
py -m pip show pandas
```

# Run the script

```
python reduce_dataset_size.py
```






