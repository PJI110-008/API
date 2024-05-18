# API
API python para consulta banco e popular o banco de dados com informações da f

## Utilizando a API

Necessário ter o docker instalado para rodar basta usar:

```sh
docker compose -f "docker-compose.yml" up -d --build
```

Isso executará os containers do python e MySQL em segundo plano a partir do Docker, ao iniciarem, a api automaticamente rodará o script de migração do banco, gerando as tables necessárias.

Após isso, basta acessar o endpoint principal:

http://localhost:5000

## Seeds

Para popular o banco, basta acessar o endpoint `/populate` que ele rodará o script de inserção dos dados do governo para o banco MySQL.
