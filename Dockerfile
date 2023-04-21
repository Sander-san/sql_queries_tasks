#FROM postgres
#
#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/
#
#COPY . /usr/src/app/
#
#RUN docker exec -it postgres psql -U postgres
#RUN CREATE DATABASE pagila;
#RUN \q
#RUN cat /pagila/pagila-schema.sql | docker exec -i postgres psql -U postgres -d pagila
#RUN cat /pagila/pagila-data.sql | docker exec -i postgres psql -U postgres -d pagila
#RUN docker exec -it postgres psql -U postgres




#FROM python:3.8
#
#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/
#
#COPY . /usr/src/app/
#RUN pip install --no-cashe-dir -r requirements.txt
#
#CMD ["python", "script.py"]




# run with port
# docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=secret -d postgres
