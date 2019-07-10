from django.db import models

# Create your models here.
class User_info(models.Model):
    user_id=models.CharField(max_length=250,default="")
    Name_title = models.CharField(max_length=250, default="")
    Name = models.CharField(max_length=250, default="")
    Password = models.CharField(max_length=250, default="")
    Address= models.CharField(max_length=250, default="")
    Contact = models.CharField(max_length=250, default="")
    Email = models.CharField(max_length=250, default="")

class Room(models.Model):
    user_id = models.CharField(max_length=250, default="")
    offer_id = models.CharField(max_length=250, default="")
    checkin = models.CharField(max_length=250, default="")
    checkout = models.CharField(max_length=250, default="")
    room_number = models.CharField(max_length=250, default="")
    stay_nights = models.CharField(max_length=250, default="")
    Floor = models.CharField(max_length=250, default="")
    Name = models.CharField(max_length=250, default="")
    Name_title = models.CharField(max_length=250, default="")

class Hotel(models.Model):
    Address= models.CharField(max_length=250, default="")
    Contact= models.CharField(max_length=250, default="")

class Hotel_Offer(models.Model):
    offer_id = models.CharField(max_length=250, default="")
    Name_title = models.CharField(max_length=250, default="")
    details = models.CharField(max_length=250, default="")

class Checkout(models.Model):
    Payment = models.CharField(max_length=250, default="")
   checkout = models.CharField(max_length=250, default="")