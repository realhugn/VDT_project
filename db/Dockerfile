FROM postgres:14-alpine

# Expose port
EXPOSE 5432

ENV POSTGRES_DB=pythondb
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=123

COPY users.csv /docker-entrypoint-initdb.d/users.csv
COPY init-db.sh /docker-entrypoint-initdb.d/init-db.sh

RUN chmod +x /docker-entrypoint-initdb.d/init-db.sh
