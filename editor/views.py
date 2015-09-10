#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core import serializers
from django.contrib.gis.geos import Polygon
from .models import Varsinaissuomenpalvelut


def index(request):
    if request.method == 'GET':
        #get request
        data = request.GET
        #set bounding box
        #bbox = (data.get("sw_lon", "0"), data.get("sw_lat", "0"), data.get("ne_lon", "0"), data.get("ne_lat", "0"))
        xmin = data.get("sw_lon", "0")
        ymin = data.get("sw_lat", "0")
        xmax = data.get("ne_lat", "0")
        ymax = data.get("ne_lon", "0")
        bbox = (xmin, ymin, xmax, ymax)
        polygon = Polygon.from_bbox(bbox)
        #get points which are contained in the bounding box
        palvelut = Varsinaissuomenpalvelut.objects.filter(geom__within=polygon)
        all_points = Varsinaissuomenpalvelut.objects.all()
        #convert to geojson
        jsonit = serializers.serialize('geojson', palvelut)
        variables = {
            'palvelut': jsonit,
            'geom': polygon,
            'all_points': all_points,
            }
        template = 'editor/index.html'
        #return to sender
        return render_to_response(template, variables)

def palvelut_json(request):
    palvelut = Varsinaissuomenpalvelut.objects.all()[:50]
    jsonit = serializers.serialize('geojson', palvelut, geometry_field='geom.geojson')
    jsonit = []
    for p in palvelut:
        jsonit.append({'nimi': p.nimi, 'geom': json.loads(p.geom.geojson)})
    variables = {
        'palvelut': palvelut,
    }
    return HttpResponse(json.dumps(jsonit, indent=1), content_type='text/plain')
