from instagram import client, subscriptions

CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': 'cab4fd643e2d42e082f1a40ee3f51c4a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)


#Zao: lat=-0.192040, lng=-78.487632
#Quicentro: lat=-0.176575,lng=-78.479613

search = unauthenticated_api.location_search(lat=-0.194259, lng=-78.484655,distance=5000)


results = []

for item in search:
	results.append(item.id)

for location_id in results:
	print unauthenticated_api.location(location_id).name, "\n"



#location = unauthenticated_api.location(location_id=20742656)
#print location.name


# Zao Oriental cusine id: 8844889


location_photos = unauthenticated_api.location_recent_media(count=20,location_id=471650)
lp=location_photos
#print location_photos

photos = []
for media in location_photos[0]:
	photos.append(media.images['standard_resolution'].url)

#print ''.join(photos)

#import ipdb; ipdb.set_trace()


# photos = []
# for media in place:
# 	photos.append('<img src="%s"/>' % media.images['thumbnail'].url)

# print ''.join(photos)

#follows =  unauthenticated_api.user_follows(4024302)
#print search


#import ipdb; ipdb.set_trace()
# for media in search:
# 	print media.images