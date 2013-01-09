from instagram import client, subscriptions

#Instagram app configuration parameters
CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': 'cab4fd643e2d42e082f1a40ee3f51c4a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

#Creating Instagram unauthenticated API object.
api = client.InstagramAPI(**CONFIG)


def search_places_by_latlng(lat,lng,distance):
	"""Returns a list of places (names and ids) that are located within a distance of the provided lat and lng
sample coordinates: near Quicentro Shopping: (-0.176575,-78.479613,5000)"""
	
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


def get_location_name(location_id):
	"""Returns a location name given a location_id"""
	location = api.location(location_id=location_id)
	return location.name


def get_location_photos(location_id, count):
	"""Returns a list of most recent photos for the given location"""	
	location_photos = api.location_recent_media(location_id=location_id, count=count)
	photos = []
	for media in location_photos[0]:
		photos.append(media.images['standard_resolution'].url)
	return photos	


print search_places_by_latlng(-0.18058746955729177,-78.46804618835449,5000)

