from django.contrib import admin
from .models import Travelpackage

# Register your models here.
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'location', 'price_per_person', 'start_date', 'end_date')
    search_fields = ('name', 'includes')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'


admin.site.register(Travelpackage, TravelPackageAdmin)