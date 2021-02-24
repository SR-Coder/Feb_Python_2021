from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# create your managers here
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['fName'])<2:
            errors['fName']= 'First name must be greater than 2 characters'
        if len(postData['lName'])<2:
            errors['lName']= 'Last name must be greater than 2 characters'
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']):
            errors['email'] = "This address is already assicoated with an account!!"
        if len(postData['password'])<8:
            errors['password'] = 'Your password is less than 8 characters'
        if postData['password'] != postData['chkPassword']:
            errors['chkPassword'] = 'Passwords Dont Match!!!'
        return errors
    def login_validator(self,postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if not User.objects.filter(email=postData['email']):
            errors['email'] = "email or password is invalid"
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()