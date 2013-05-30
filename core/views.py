# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Location, Category
from core.forms import SearchLocationsForm
import photos

def app_index(request):
	locations = Location.objects.all().order_by('name')
	categories = Category.objects.all().order_by('name')

	context = {'locations': locations, 'categories': categories}
	
	return render_to_response(
		'index.html',
		context,
		context_instance=RequestContext(request))

def location_page(request,locationslug):
	locations_all = Location.objects.all().order_by('name')
	location = Location.objects.get(slug=locationslug)
	categories = Category.objects.all().order_by('name')
	location_photos = photos.get_location_photos(
		count=30, location_id=location.instagram_id)

	context = {
		'location': location,
		'locations_all': locations_all,
		'categories': categories,
		'photos': location_photos}

	return render_to_response(
		'location.html', context, context_instance=RequestContext(request))

def search_locations(request):
	if request.method == 'POST':
		form = SearchLocationsForm(request.POST)
        if form.is_valid():

        	lat = form.cleaned_data['lat']
        	lng = form.cleaned_data['lng']
        	distance = form.cleaned_data['distance']

        	locations_search_results = photos.search_places_by_latlng(
        		lat=lat, lng=lng, distance=distance)

        	context = {'locations': locations_search_results}

        	return render_to_response(
        		'search_locations.html',
        		context,
        		context_instance=RequestContext(request)) 
    	else:
    		form = SearchLocationsForm() # An unbound form
    		context = {'form': form}
    		return render_to_response(
				'search_locations.html', context,
				context_instance=RequestContext(request))
