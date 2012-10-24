from django.db import models


class Tag (models.Model):
	tag_name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.tag_name

class Location (models.Model):
	location_name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.location_name

class Geography (models.Model):
	latitude = models.CharField(max_length=100)
	distance = models.CharField(max_length=100)	
	longitude = models.CharField(max_length=100)	
	
	def __unicode__(self):
		return "Latitude: " + self.latitude + " Distance: "
		+ self.distance + "Longitude: " + self.longitude

class Map (models.Model):
	map_name = models.CharField(max_length=100)
	a_geography = models.ForeignKey(Geography)

	def __unicode__(self):
		return self.map_name

class User (models.Model):
	user_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __unicode__(self):
		return self.user_name

class Place (models.Model):
	country = models.CharField(max_length=100)
	province = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	a_geography = models.ForeignKey(Geography, blank=True)
	a_location = models.ForeignKey(Location, blank=True)
	a_tag = models.ForeignKey(Tag, blank=True)

	def __unicode__(self):
		return "country: " + self.country + " province: "
		+ self.province + "city: " + self.city
