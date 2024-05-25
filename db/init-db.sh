#!/bin/bash
set -e

# Wait for PostgreSQL to start
until psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\l'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  gender TEXT,
  university TEXT,
  phone TEXT
);
EOSQL

# Load data from CSV
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\COPY users(name, gender, university, phone) FROM '/docker-entrypoint-initdb.d/users.csv' DELIMITER ',' CSV HEADER;"