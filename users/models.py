# users/models.py

from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    api_key= models.CharField(max_length=10)

def __str__(self):
        return f'User {self.username} email: {self.email} with display name: {self.display_name}'
