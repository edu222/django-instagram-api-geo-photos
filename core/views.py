# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Location
from instagram import client

#Instagram app configuration parameters
CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': 'cab4fd643e2d42e082f1a40ee3f51c4a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

#Instagram unauthenticated api object.
instagram_api = client.InstagramAPI(**CONFIG)


def app_index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def location_page(request,locationslug):
	location = Location.objects.get(slug=locationslug)
	location_recent_media = instagram_api.location_recent_media(count=19,location_id=location.instagram_id)

	photos = []
	for media in location_recent_media[0]:
		photos.append(media.images['standard_resolution'].url)

	
	context = {'location': location, 'photos': photos}
	return render_to_response('location.html', context, context_instance=RequestContext(request))

