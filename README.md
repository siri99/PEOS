IS5009 Final Project


PostgreSQL

* CREATE USER is5009 WITH PASSWORD 'is5009pw123';
* CREATE DATABASE peos_db;
* ALTER ROLE is5009 SET client_encoding TO 'utf8';
* ALTER ROLE is5009 SET default_transaction_isolation TO 'read committed';
* ALTER ROLE is5009 SET timezone TO 'UTC';
* GRANT ALL PRIVILEGES ON DATABASE PEOS_DB TO is5009;
* ALTER USER is5009 CREATEDB;


Django Create Superuser to access Django Admin Page
python manage.py createsuperuser --username=is5009 --email=is5009@gmail.com