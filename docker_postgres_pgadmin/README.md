# Docker Postgres PGadmin

- 
```
cd docker_postgres_pgadmin
```

- 
```
echo *data/ >> .gitignore
```

- 
```
docker-compose up
```

- 
```
docker-compose down
```

- 
```
docker container ls
```

- 
```
docker inspect container_id
```

- Create new server in PGAdmin4:
    - Gives the name of the new server to postgres_database;
    - Execute docker inspect container_id to get the IP address;
    - Choose the dataase;
    - Informs the user and password;

# Creates Database

# Connects to new Database

# Creates User

# Grants Privileges

# Connects to new Database with new User

# Creates the tables

# Loads the file

```
FROM dpage/pgadmin4:latest
COPY data .
```

# References

- How to create a docker-compose setup with PostgreSQL and pgAdmin4. [S. L.], 2023. 1 vídeo (7 minutos). Publicado pelo canal Random Code. Disponível em: https://www.youtube.com/watch?v=qECVC6t_2mU. Acesso em: 19 de Março de 2024.

- https://www.prisma.io/dataguide/postgresql/authentication-and-authorization/role-management

- https://www.sqliz.com/postgresql/show-databases/#:~:text=There%20are%20two%20methods%20to%20list%20all%20the,2%20Query%20all%20databases%20from%20the%20pg_database%20table.