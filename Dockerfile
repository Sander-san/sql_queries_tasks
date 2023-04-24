FROM postgres

#ENV POSTGRES_PASSWORD=$DB_PASSWORD
#ENV POSTGRES_DB=$DATABASE

ENV POSTGRES_PASSWORD secret
ENV POSTGRES_DB pagila

COPY ./pagila-schema.sql /docker-entrypoint-initdb.d/
COPY ./pagila-data.sql /docker-entrypoint-initdb.d/
COPY ./init.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/init.sh

CMD ["postgres"]






