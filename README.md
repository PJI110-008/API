# API
API python para consulta banco e popular o banco de dados com informações da fonte de dados externa

## Criando tables do Banco

Rodar o seguinte script ao conectar no banco pela primeira vez:

```sql
CREATE TABLE 9756_idade_cor_ou_raca (
    id SERIAL PRIMARY KEY,
    Cor_ou_raca VARCHAR(100),
    Grande_Regiao VARCHAR(100),
    Ano VARCHAR(100),
    Porcentagem INTEGER
);
```

## Utilizando a API

Necessário ter o docker instalado para rodar basta usar:

```sh
docker compose -f "docker-compose.yml" up -d --build
```

Isso executará os containers do python e MySQL em segundo plano a partir do Docker, para criar as tables do banco é só seguir do tutorial acima, e para popular os dados basta rodar o seguinte script:

```sh
docker compose exec api python consultaAPI_9756.py
```

Após isso, basta acessar o endpoint principal:

http://localhost:5000

## Migrations

```bash
# python manage.py db init # initializing the database
python manage.py db migrate
python manage.py db upgrade
```
