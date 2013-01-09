from django.db import models

class Location (models.Model):
	name = models.CharField(max_length=100)
	instagram_id = models.IntegerField(max_length=100) 
	city = models.ForeignKey('City')
	slug = models.SlugField()
	category = models.ForeignKey('Category')

	def __unicode__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=100)
	country = models.ForeignKey('Country')

	def __unicode__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name	