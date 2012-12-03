from instagram import client, subscriptions

CONFIG = {
    'client_id': '83d1b794dfc24f5588378f88be67c586',
    'client_secret': 'cab4fd643e2d42e082f1a40ee3f51c4a',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)



#popular = unauthenticated_api.media_popular()
search = unauthenticated_api.media_search(4,12,-0.176575,-78.479613)
for item in search:
	print item

photos = []
for media in search:
	photos.append('<img src="%s"/>' % media.images['thumbnail'].url)

print ''.join(photos)

#follows =  unauthenticated_api.user_follows(4024302)
#print search