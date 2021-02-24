from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')


# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['fName'])<2:
            errors['fName']= 'First name must be longer than 2 characters'
        if len(postData['lName'])<2:
            errors['lName']= 'Last name must be longer than 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='provide a valid email address'
        if len(postData['password'])<8:
            errors['password']='Your password must be longer than 8 characters'
        if postData['password'] != postData['chkPassword']:
            errors['chkPassword']='your passwords dont match'
        return errors
    def login_validator(self, postData):

        return errors




class User(models.Model):
    # id = gives it a unique integer
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #snowBananas dont forget the .all()
    #likedSnowBananas dont forget the .all()
    # string that is returned when we want to view the object
    def __str__(self):
        s = '\n'
        s += f'first_name: {self.first_name}\n'
        s += f'last_name: {self.last_name}\n'
        s += f'email: {self.email}\n'
        return s
    
class SnowBanana(models.Model):
    color = models.CharField(max_length=255)
    ripeness = models.CharField(max_length=255)
    age = models.IntegerField()
    user = models.ForeignKey(User, related_name="snowbananas", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='likedSnowBananas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)