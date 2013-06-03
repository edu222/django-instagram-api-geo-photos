import os
from instagram import client, subscriptions

try:
	from core_keys import insta_secret
except ImportError:
	insta_secret = os.environ['INSTAGRAMSECRET']
	

#Instagram app configuration parameters
CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': insta_secret,
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

#Creating Instagram unauthenticated API object with the config.
api = client.InstagramAPI(**CONFIG)


def search_places_by_latlng(lat,lng,distance):
	"""Returns a list of places (names and ids) that are located within
	   a distance of the provided lat and lng.
       Sample coordinates near 'Quicentro mall':(-0.176575,-78.479613,5000)"""
	
	#Searching location
	search = api.location_search(lat=lat, lng=lng,distance=distance)
	
	#Creating a list of loction id's based on search results
	location_id_list = []

	for location in search:
		location_id_list.append(location.id)

	#Creating a list of location names and id's corresponding to the search.
	places = []
	for location_id in location_id_list:
		location_string = api.location(location_id).name,location_id
		places.append(location_string)	

	return places

def search_places_by_foursquare_v2_id(foursquare_v2_id):
	"""Returns a list of places (names and ids) that are located within
	   a distance of the provided lat and lng."""

	#Searching location
	search = api.location_search(foursquare_v2_id=foursquare_v2_id)
	
	#Creating a list of loction id's based on search results
	location_id_list = []

	for location in search:
		location_id_list.append(location.id)

	#Creating a list of location names and id's corresponding to the search.
	places = []
	for location_id in location_id_list:
		location_string = api.location(location_id).name,location_id
		places.append(location_string)	

	return places



def get_location_name(location_id):
    """Returns a location name given a location_id"""
    try:
        location_id = int(location_id)
    except ValueError:
        return None
    
    location = api.location(location_id=location_id)
    return location.name


def get_location_photos(location_id, count):
	"""Returns a list of most recent photos for the given location"""	
	location_photos = api.location_recent_media(location_id=location_id,
												count=count)
	photos = []
	for media in location_photos[0]:
		photos.append(media.images['standard_resolution'].url)
	return photos	


print search_places_by_foursquare_v2_id(
	foursquare_v2_id='4b9941f1f964a5202c6e35e3')


