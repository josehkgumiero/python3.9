import json

from flask import Flask, render_template

app = Flask(__name__)

import os


# Atribuindo valor a variável da senha
######################################################################################

_POSTGRES_PASSWORD_FILE = """"POSTGRES_PASSWORD_FILE""" 
_OS_ENVIRON = os.environ
_READ = """r"""
_POSTGRES_PASSWORD = """POSTGRES_PASSWORD"""

if _POSTGRES_PASSWORD_FILE in _OS_ENVIRON:
    with open(_OS_ENVIRON[_POSTGRES_PASSWORD_FILE], _READ) as _OPEN_FILE:
        _PASSWORD = _OPEN_FILE.read().strip()
        _PASSWORD_FROM = 'FILE'
else:
    _PASSWORD = _OS_ENVIRON[_POSTGRES_PASSWORD]
    _PASSWORD_FROM = 'ENVIRONMENT'


# Rota padrão Hello World
######################################################################################

@app.route("""/""")
def _hello_world():
    return "{0} {1}".format(_USER, _PASSWORD)

# Rota de iniciar banco de dados
######################################################################################

import psycopg2

_HOST = """db"""
_USER = """postgres"""
_DATABASE = """example"""
_DROP_DATABASE_IF_EXISTS = """DROP DATABASE IF EXISTS example"""
_CREATE_DATABASE = """CREATE DATABASE example"""

_SELECT_ALL = """SELECT * FROM widgets"""

@app.route("""/init_database""")
def _database_init():

    # conexão com host, user, password
    _connect = psycopg2.connect(
        host = _HOST,
        user = _USER,
        password = _PASSWORD
    )

    # autocommit para conexão
    _connect.set_session(autocommit = True)

    # deleta e cria o banco de dados
    with _connect.cursor() as _cursor:
        _cursor.execute(_DROP_DATABASE_IF_EXISTS)
        _cursor.execute(_CREATE_DATABASE)
    _connect.close()

    return """init database"""

# Rota padrão telnet do banco de dados
######################################################################################

@app.route("""/telnet""")
def _telnet():
    _connect = psycopg2.connect(
        host = _HOST,
        user = _USER,
        password = _PASSWORD,
        database = _DATABASE
    )
    
    return "Connected"


# Rota de iniciar tabela
######################################################################################

_DROP_TABLE_IF_EXISTS = """DROP TABLE IF EXISTS widgets"""
_CREATE_TABLE = """CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))"""

@app.route("""/init_table""")
def _table_init():

    with psycopg2.connect(
        host = _HOST,
        user = _USER,
        password = _PASSWORD,
        database = _DATABASE
    ) as _connect:
        with _connect.cursor() as _cursor:
            _cursor.execute(_DROP_TABLE_IF_EXISTS)
            _cursor.execute(_CREATE_TABLE)
    _connect.close()

    return """init table"""

@app.route("""/insert""")
def _insert_values():
    _connect = psycopg2.connect(
        host = _HOST,
        user = _USER,
        password = _PASSWORD,
        database = _DATABASE
    )

    _cursor = _connect.cursor()

    _cursor.execute(
        'INSERT INTO widgets (name, description)'
        'VALUES (%s, %s)',
        (
            'Jose',
            'Lindo'
        )
    )

    _connect.commit()

    _cursor.close()

    _connect.close()

    return "Inserted"

@app.route("""/widgets""")
def _gwg():
    with psycopg2.connect(
        host = _HOST,
        user = _USER,
        password = _PASSWORD,
        database = _DATABASE
    ) as _connect:
        with _connect.cursor() as _cursor:
            _cursor.execute(_SELECT_ALL)
            _row_header = [x[0] for x in _cursor.description]
            _results = _cursor.fetchall()
    _connect.close()

    _json_data = [dict(zip(_row_header, _result)) for _result in _results]

    return json.dumps(_json_data)



if __name__ == "__main__":
    app.run(host = '0.0.0.0')