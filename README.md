# Aula 16 - Usando PostgreSQL


## Rodando postgres no docker

```shell
docker run --name postgres-db -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:14
```