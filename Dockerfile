FROM postgres:latest
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
COPY ./scripts/schema.sql /docker-entrypoint-initdb.d/