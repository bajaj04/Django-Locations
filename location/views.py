from django.utils.translation import ugettext
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from .forms import LocationForm
from .models import Country,State,City

def locations(request):
    form = LocationForm
    variables = RequestContext(request, {
        'form' : form
        })
    return render_to_response('location/locations.html', variables)

def country_state_list_ajax(request):
    if request.POST.has_key('country'):
        country = get_object_or_404(Country,id=request.POST['country'])
        states = country.state_set.all()
        return render_to_response('location/ajax/country_state_list_ajax.html', {'states' : states})
def state_city_list_ajax(request):
    if request.POST.has_key('state'):
        state = get_object_or_404(State,id=request.POST['state'])
        cities = state.city_set.all()
        return render_to_response('location/ajax/state_city_list_ajax.html', {'cities' : cities})

def add_country_ajax(request):   
    if request.POST.has_key('iso2_code') and request.POST.has_key('name') and request.POST.has_key('printable_name') and request.POST.has_key('iso3_code') and request.POST.has_key('numcode') and request.POST.has_key('continent'):
        country = Country()
        country.iso2_code = request.POST['iso2_code']
        country.name = request.POST['name']
        country.printable_name = request.POST['printable_name']
        country.iso3_code = request.POST['iso3_code']
        country.numcode = request.POST['numcode']
        country.continent = request.POST['continent']
        country.save()
        contries = Country.objects.all()
        return render_to_response('location/ajax/add_country_ajax.html', {'contries' : contries,'country':country})

def add_state_ajax(request):   
    if request.POST.has_key('country') and request.POST.has_key('state'):
        country = get_object_or_404(Country,id=request.POST['country'])
        state = State()
        state.country = country
        state.name = request.POST['state']
        state.save()
        states = State.objects.all()
        return render_to_response('location/ajax/add_state_ajax.html', {'state' : state,'states':states})
def add_city_ajax(request):   
    if request.POST.has_key('country') and request.POST.has_key('state') and request.POST.has_key('city'):
        country = get_object_or_404(Country,id=request.POST['country'])
        state = get_object_or_404(State,id=request.POST['state'])
        city = City()
        city.country = country
        city.state = state
        city.name = request.POST['city']
        city.save()
        cities = City.objects.filter(state=state)
        return render_to_response('location/ajax/add_city_ajax.html', {'cities' : cities,'city':city})
