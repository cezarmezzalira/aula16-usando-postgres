# Aula 16 - Usando Poetry e PostgreSQL 

A partir das próximas aulas, vamos tornar nosso projeto mais robusto, adicionando nele uma estrutura mais organizada, começando com o uso do Poetry para gerenciar nossas dependências.

## Instalando o poetry

Siga o passo a passo conforme seu sistema operacional no link a seguir:
<https://python-poetry.org/docs/#installing-with-the-official-installer>

## Configurar o poetry para criar o .venv dentro da pasta do projeto

```shell
poetry config virtualenvs.in-project true
```


## Criando o arquivo pyproject.toml

O Poetry usa um arquivo chamado `pyproject.toml`, o qual é responsável por armazenar todas as configurações de dependência, tipo de licença, nome do projeto, versão atual, entre outras.

Para criar o arquivo, basta executar o comando abaixo e ir respondendo as perguntas:


```shell
poetry init
```

## Instalando as dependências do projeto

```shell
poetry add fastapi=0.104.1 uvicorn=0.24.0 sqlmodel=0.0.11 psycopg2-binary=2.9.9
```

## Rodando postgres no docker

```shell
docker run --name postgres-db -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:14
```

## Configurando a estrutura do projeto

```shell
.
├── .gitignore
├── README.md
├── pyproject.toml
└── src/
    ├── config/
    │   └── database.py
    ├── main.py
    └── models/
        └── manutencao_model.py
```
