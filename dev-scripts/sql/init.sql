CREATE DATABASE cherno;
CREATE USER cherno WITH PASSWORD 'cherno';
ALTER ROLE cherno SET client_encoding TO 'utf8';
ALTER ROLE cherno SET default_transaction_isolation TO 'read committed';
ALTER ROLE cherno SET timezone TO 'UTC';
