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

def index(request):


    """
    if request.method == 'GET':
        points = Varsinaissuomenpalvelut.objects.all()[:50]
        serializer = ServiceDataSerializer(points, many=True)
        pagination_class = GeoJsonPagination
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceDataSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
class services(generics.ListAPIView):
    queryset = Varsinaissuomenpalvelut.objects.all()
    serializer_class = ServiceDataSerializer
    pagination_class = GeoJsonPagination
    filter_backends = (InBBoxFilter,filters.DjangoFilterBackend,)
    filter_fields = ('kohde',)
    #filter_backends = (InBBoxFilter, )
    bbox_filter_field = 'geom'
    bbox_filter_include_overlapping = True
