# mapedit

[![Join the chat at https://gitter.im/ekohalsti/mapedit](https://badges.gitter.im/ekohalsti/mapedit.svg)](https://gitter.im/ekohalsti/mapedit?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Mapeditor

Requirements:
 - Postgresql-dev (Ubuntu: postgresql-server-dev-<version>),
 - PostGIS (Ubuntu: postgresql-<version>-postgis-2.1, postgis),
 - Python 3,
 - Python-dev,
 - psycogp2

Create database:
- createdb open_data;psql open_data
- CREATE EXTENSION postgis;

Database creation using shp2pgsql:
 - Use the name of the db & user as parameters here.
 - shp2pgsql -IiSD -s 3067 -g geom -W LATIN1 varsinaissuomenpalvelut.shp > palvelut.sql;psql -U user -W database < palvelut.sql
