#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

from .models import Varsinaissuomenpalvelut

def index(request):
    palvelut = Varsinaissuomenpalvelut.objects.all()[:50]
    variables = {
        'palvelut': palvelut,
    }
    template = 'editor/index.html'
    return render_to_response(
        template, variables)

def palvelut_json(request):
    palvelut = Varsinaissuomenpalvelut.objects.all()[:50]
    jsonit = []
    for p in palvelut:
        jsonit.append({'nimi': p.nimi, 'geom': json.loads(p.geom.geojson)})
    variables = {
        'palvelut': palvelut,
    }
    return HttpResponse(json.dumps(jsonit, indent=1), content_type='text/plain')
