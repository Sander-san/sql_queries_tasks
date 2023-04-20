FROM postgres:latest

ENV POSTGRES_PASSWORD=secret

EXPOSE 5432

COPY pagila-schema.sql /docker-entrypoint-initdb.d/
COPY pagila-data.sql /docker-entrypoint-initdb.d/

CMD ["python", "script.py"]
