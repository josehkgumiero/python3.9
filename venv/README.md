# VENV

- Python Vitrtual Environments;
- It is a module;
- This creates lightweight "virtual environments"; 
- Allow install packages in an isolated location (site direcories);
- Inside the VENV, the pip is not needing to be told to do so explicity;
- The project implementation should contain only the python packages needed for application;
- It's important to manage third-party packages;
- There is a conflict of package versions between different projects, managing separately is a pratical solution;
- Using a requirements.txt, it can define exact version number for the required packages;
- This also helps reproduce the version of the project to test like and the packages too;
- The VENV can manages the packages in or development, or build, or production environments;
- Other options: poetry, pipenv;
- This command creates a venv in the specified directory and copies pip into it as well. If you’re unsure what to call the directory: venv is a commonly seen option;
```
mkdir <directory>
```
```
cd <directory>
```
```
python -m venv <directory>\venv
```
```
python -m venv <directory>\venv --system-site-packages
```
```
echo <directory>\venv > .gitignore
```
```
echo .env >> .gitignore
```
- To activate
```
# In cmd.exe
<directory>\venv\Scripts\activate.bat
```
```
# In PowerShell
<directory>\venv\Scripts\Activate.ps1
```
```
py -m pip freeze > requirements.txt
```
```
pip install -r requirements.txt
```
```
pip list
```
```
py -m pip list
```
```
pip install request==2.30.0
```
```
py -m pip install request==2.30.0
```
```
pip list
```
```
py -m pip list
```
```
py -m pip uninstall requests
```
- Example of install packages
```
py -m pip install requests
```
```
py -m pip list
```
- Looks to requires packages that are installed too
```
py -m pip show requests
```
- Just enter this: 
```
deactivate
```
- Remove the venv path created with the venv command
```
# If your virtual environment is in a directory called 'venv':
rm -r venv
```

# PyPi

# References

- Python Tutorial: VENV (Windows) - How to Use Virtual Environments with the Built-In venv Module. [S. L.], 2022. 1 vídeo (17 minutos). Publicado pelo canal Corey Schafer. Disponível em: https://www.youtube.com/watch?v=APOPm01BVrk. Acesso em: 17 de Março de 2024.

- Python Virtual Environment and pip for Beginners. [S. L.], 2023. 1 vídeo (31 minutos). Publicado pelo canal Dave Gray. Disponível em: https://www.youtube.com/watch?v=eDe-z2Qy9x4. Acesso em: 17 de Março de 2024.

- Understanding Virtual Environments for Data Science / Data Analysis - P.4. [S. L.], 2020. 1 vídeo (21 minutos). Publicado pelo canal Luke Barousse. Disponível em: https://www.youtube.com/watch?v=qI0uJsLweoM. Acesso em: 17 de Março de 2024.