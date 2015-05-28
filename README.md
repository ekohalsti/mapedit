# mapedit
Mapeditor

Requirements:
 PostgreSQL
 PostGIS
 Python 2

Database creation using shp2pgsql:
 shp2pgsql -IiSD -s 3067 -g geom varsinaissuomenpalvelut.shp > palvelut.sql
 psql -U postgres -W open_data < palvelut.sql

