from instagram import client, subscriptions

#Instagram app configuration parameters
CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': 'cab4fd643e2d42e082f1a40ee3f51c4a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

#Creating Instagram unauthenticated API object.
api = client.InstagramAPI(**CONFIG)

# Returns a list of places (names and ids) that are located within a distance of the provided lat and lng
#sample coordinates: near Quicentro Shopping: lat=-0.176575,lng=-78.479613
def search_by_place(lat,lng,distance):
	
	#Searching location
	search = api.location_search(lat=lat, lng=lng,distance=distance)
	location_id_list = []
	
	#Creating a list of loction id's based on search results
	for location in search:
		location_id_list.append(location.id)

	#Creating a list of location names and id's corresponding to the search.
	places = []
	for location_id in location_id_list:
		places.append(api.location(location_id).name,": ", location_id, "\n")	

	return places

# Returns a location name given a location_id
def get_location_name(location_id):
	location = api.location(location_id=location_id)
	return location.name


#Returns a list of most recent photos for the given location
def get_location_photos(location_id, count):
	location_photos = api.location_recent_media(location_id=location_id, count=count)
	photos = []
	for media in location_photos[0]:
		photos.append(media.images['standard_resolution'].url)
	return photos	

