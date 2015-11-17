#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.contrib.gis.geos import Polygon
from .models import Varsinaissuomenpalvelut
from django.views.decorators.csrf import csrf_exempt
from .serializers import ServiceDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework import generics
from rest_framework import filters
from rest_framework_gis.filters import InBBoxFilter

#@api_view(['GET', 'POST'])
#def index(request):

class services(generics.ListAPIView):
    queryset = Varsinaissuomenpalvelut.objects.all()
    serializer_class = ServiceDataSerializer
    pagination_class = GeoJsonPagination
    filter_backends = (InBBoxFilter,filters.DjangoFilterBackend,)
    filter_fields = ('kohde',)
    #filter_backends = (InBBoxFilter, )
    bbox_filter_field = 'geom'
    bbox_filter_include_overlapping = True
