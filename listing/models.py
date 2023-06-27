from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    
    def __str__ (self):
        return str(self.city)

class ProductAmenitiesModel(models.Model):
    Air_Conditioning = models.BooleanField(default=True)
    Balcony = models.BooleanField(default=True)
    Garden_Yard = models.BooleanField(default=True)
    Pool = models.BooleanField(default=True)
    Security_System = models.BooleanField(default=True)
    Parking_Space = models.BooleanField(default=True)
    Basement = models.BooleanField(default=True)
    BBQ_Area = models.BooleanField(default=True)
    Walk_in_Closet = models.BooleanField(default=True)
    Central_Heating = models.BooleanField(default=True)
    Deck_Patio = models.BooleanField(default=True)
    Dishwasher = models.BooleanField(default=True)
    Fireplace = models.BooleanField(default=True)
    Fitness_Center_Gym = models.BooleanField(default=True)
    Garage = models.BooleanField(default=True)
    Hardwood_Floors = models.BooleanField(default=True)
    Laundry_Room = models.BooleanField(default=True)
    Washer_Dryer_Hookups = models.BooleanField(default=True)
    Wheelchair_Accessible = models.BooleanField(default=True)
    Pet_Friendly = models.BooleanField(default=True)
    High_Speed_Internet_Access = models.BooleanField(default=True)
    Cable_Satellite_TV = models.BooleanField(default=True)
    Fully_Furnished = models.BooleanField(default=True)
    Gated_Community = models.BooleanField(default=True)
    Tennis_Basketball_Court = models.BooleanField(default=True)
    Playground = models.BooleanField(default=True)
    Elevator = models.BooleanField(default=True)
    Waterfront_Access = models.BooleanField(default=True)
    Close_to_Public_Transportation = models.BooleanField(default=True)
    Proximity_to_Schools = models.BooleanField(default=True)
    Nearby_Shopping_Restaurants = models.BooleanField(default=True)
    Access_to_Parks_Recreational_Areas = models.BooleanField(default=True)

    On_Site_Maintenance = models.BooleanField(default=True)
    On_Site_Management = models.BooleanField(default=True)

    Hour_Security = models.BooleanField(default=True)
    Energy_Efficient_Appliances = models.BooleanField(default=True)
    Green_Building_Features = models.BooleanField(default=True)
    Smart_Home_Technology = models.BooleanField(default=True)
    Outdoor_Entertaining_Area = models.BooleanField(default=True)
    Wine_Cellar = models.BooleanField(default=True)
    Home_Theater = models.BooleanField(default=True)
    Office_Study_Room = models.BooleanField(default=True)
    Guest_House_In_Law_Suite = models.BooleanField(default=True)
    Game_Room = models.BooleanField(default=True)
    Vaulted_Ceilings = models.BooleanField(default=True)
    Skylights = models.BooleanField(default=True)
    Workshop_Studio_Space = models.BooleanField(default=True)
    Solar_Panels = models.BooleanField(default=True)
    Mountain_City_View = models.BooleanField(default=True)



    def __str__(self):
        return str(self.id)

class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='ProductImage/')
    product = models.ForeignKey('ProductPropertyModel', on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    users_type = (
        ('Agent','Agent'),
        ('User','User'),
        ('Expert','Expert')
    )
    user_type = models.CharField(choices=users_type , max_length=50,default='Agent')
    profile_image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return  str(self.id)


class Agent(models.Model):
    admin = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location , on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.id)

class Customer (models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.admin)

class Expert(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.admin + ' ' + self.id)

class ProductPropertyModel(models.Model):
    tile = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    type = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    postal_Code = models.CharField(max_length=100)
    floor = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    room = models.IntegerField()
    area = models.IntegerField()
    lotarea = models.IntegerField()
    price = models.FloatField()
    grauge = models.CharField(max_length=100)
    isactive = models.BooleanField(default=True)
    medai_url = models.CharField(max_length=400)
    coverPhoto = models.ImageField(upload_to="ProductCoverPhoto/")
    amenities = models.ForeignKey('ProductAmenitiesModel', on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE , null=True)

class AgentRate (models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class WishList (models.Model):
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    product = models.ForeignKey(ProductPropertyModel, on_delete= models.CASCADE)

class ProducttRate (models.Model):
    comment = models.TextField()
    rate = models.IntegerField()
    product = models.ForeignKey(ProductPropertyModel, on_delete= models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

class AgentMessage(models.Model):
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    service = models.CharField(max_length=200)
    propType = models.CharField(max_length=200)
    message = models.TextField()
    agent = models.ForeignKey(Agent , on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)