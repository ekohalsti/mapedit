# mapedit
Mapeditor

Requirements:
 PostgreSQL,
 PostGIS,
 Python 2,
 Python-dev,
 PostgreSQL-dev,
 psycogp2

Create database:
- createdb open_data;psql open_data
- CREATE EXTENSION postgis;
- default user is postgres
- default password is test123

Database creation using shp2pgsql:
 - Use the name of the db & user as parameters here.
 - shp2pgsql -IiSD -s 3067 -g geom -W LATIN1 varsinaissuomenpalvelut.shp > palvelut.sql;psql -U user -W database < palvelut.sql

