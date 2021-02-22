from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SnowBanana(models.Model):
    color = models.CharField(max_length=255)
    ripeness = models.CharField(max_length=255)
    age = models.IntegerField()
    user = models.ForeignKey(User, related_name="snowbananas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)