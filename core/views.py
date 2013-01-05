# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Location
import photos

def app_index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def location_page(request,locationslug):
	location = Location.objects.get(slug=locationslug)
	location_photos = photos.get_location_photos(count=20,location_id=location.instagram_id) 

	context = {'location': location, 'photos': location_photos}
	return render_to_response('location.html', context, context_instance=RequestContext(request))

