from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Country, State, City


class StateInline(admin.TabularInline):
    model = State
    extra = 1
class CityInline(admin.TabularInline):
    model = City
    extra = 1

class CountryAdmin(admin.ModelAdmin):
 
    

    list_display = ('printable_name', 'iso2_code')
    search_fields = ('name', 'iso2_code', 'iso3_code')
    inlines = [StateInline]

admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
 
    list_display = ('name', 'abbr','country')
    list_filter = ('country',)
    search_fields = ('name', 'abbr')
    inlines = [CityInline]

admin.site.register(State, StateAdmin)
    
class CityAdmin(admin.ModelAdmin):
 
    list_display = ('name', 'abbr','state','country')
    list_filter = ('country','state')
    search_fields = ('name', 'abbr')
    
admin.site.register(City, CityAdmin)