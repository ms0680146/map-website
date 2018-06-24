from django.db import models
from nccu.settings import *

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=20,null=True,blank=True)
	address = models.CharField(max_length=50,null=True,blank=True)
	opentime = models.CharField(max_length=50,null=True,blank=True)
	longitude = models.FloatField(null=True,blank=True,default=None)
	latitude = models.FloatField(null=True,blank=True,default=None)
	
	def __str__(self):
		return '%s %s %s %s %s %s' %(self.name,self.phone_number,self.address,self.opentime,self.longitude,self.latitude)
		
class Comment(models.Model):
	content=models.CharField(max_length=255)
	user=models.CharField(max_length=255)
	date_time=models.DateTimeField()
	restaurant=models.ForeignKey(Restaurant)
	
class Photo(models.Model):
	store = models.ImageField(upload_to = UPLOAD_ROOT)
	storename = models.ForeignKey(Restaurant)
