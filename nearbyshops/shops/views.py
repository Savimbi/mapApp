from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
import json
from django.core import serializers

longitude = 34.6909267
latitude = 135.5049973

user_location = Point(longitude, latitude, srid=4326)

def index(request):
    listings = Shop.objects.values('location','name').annotate(distance=Distance('location', user_location)).order_by('distance')[:6]
    print(listings[0])
    
    
    context = {
        'listings': listings
    }
    return render(request, 'shops/index.html', context)

# class Home(generic.ListView):
#     model = Shop
#     context_object_name = 'shops'
#     Queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:6]
#     #Queryset = Shop.objects.filter(location__distance_lte=(user_location,D(km=8)))[0:5]
#     print(Queryset[2].location.x)
#     print(Queryset[2].location.y)
#     template_name = 'shops/index.html'


# Create your views here.
