from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Feature (models.Model):
    floor = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    garauge = models.IntegerField()
    area = models.FloatField()
    lotarea = models.FloatField()
    price = models.FloatField()
    extraroom = models.IntegerField()
    coverimage = models.ImageField(upload_to='coverImage/')
    image = models.ImageField(upload_to='apartmentImage/')

class Product (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length = 500)
    product_type = models.IntegerField()
    status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location , on_delete= models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete= models.CASCADE)

class AmenitiesAdmin (models.Model):
    name = models.CharField(max_length=50)

class AmenitiesAddListing (models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    amenities = models.ForeignKey(AmenitiesAdmin , on_delete= models.CASCADE)

class CustomUser(AbstractUser):
    users_type = (
        (1,'Agent'),
        (2,'User'),
        (3,'Expert')
    )
    user_type = models.CharField(choices=users_type , max_length=50,default=2)
    profile_image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return  str(self.id)


class WishList (models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)

class ProducttRate (models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)


class Agent(models.Model):
    admin = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location , on_delete=models.CASCADE)

class Customer (models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Expert(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class AgentRate (models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)