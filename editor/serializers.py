from rest_framework import serializers
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from .models import Varsinaissuomenpalvelut
from rest_framework_gis.pagination import GeoJsonPagination

class ServiceDataSerializer(GeoFeatureModelSerializer):

    class Meta:
        geo_field = 'geom'
        id_field = 'gid'
        model = Varsinaissuomenpalvelut
        fields = ('gid', 'kohde', 'postinumer', 'kunta', 'nimi', 'aukiolo',
        'lis_tiedot', 'katuosoite', 'kuntanro', 'kohdenro', 'paikkaluku',
        'julkpalvel', 'wwwlinkki', 'timestamp', 'paivittaja', 'puhelin', 'visual',
        'legend', 'postinro', 'kohde2')
        auto_bbox = True
