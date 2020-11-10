from django.contrib.gis import admin
from .models import Shop

# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.OSMGeoAdmin):
    last_display = ['name', 'location']