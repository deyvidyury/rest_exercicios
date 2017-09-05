from django.contrib.auth.models import User
from django.db import models

class Geo(models.Model):
  lat = models.FloatField()
  lng = models.FloatField()

  def __str__(self):
    return self.lat + ", " + self.lng

class Address(models.Model):
  street = models.CharField(max_length=300)
  suite = models.CharField(max_length=100)
  city = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=100)
  geo = models.ForeignKey(Geo, on_delete = models.CASCADE)

class Company(models.Model):
  name = models.CharField(max_length=200)
  catchPhrase = models.CharField(max_length=200)
  bs = models.CharField(max_length=200)

class UserExt(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # name = models.CharField(max_length=200)
  # username = models.CharField(max_length=100)
  # email = models.EmailField(max_length=200)
  address = models.ForeignKey(Address, on_delete = models.CASCADE)
  phone = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  company = models.ForeignKey(Company, on_delete = models.CASCADE)

class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  owner = models.ForeignKey('auth.User',related_name='games',on_delete=models.CASCADE)

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments")
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  body = models.TextField()

  def __str__(self):
    return self.name + ", email: " + self.email + ", said: " + self.body 

