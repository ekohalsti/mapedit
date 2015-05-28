# mapedit
Mapeditor

Requirements:
 PostgreSQL,
 PostGIS,
 Python 2

Database creation using shp2pgsql:
 Create user & database. Use the name of the db & user as parameters here.
 shp2pgsql -IiSD -s 3067 -g geom varsinaissuomenpalvelut.shp > palvelut.sql|psql -U <user> -W <database> < palvelut.sql

