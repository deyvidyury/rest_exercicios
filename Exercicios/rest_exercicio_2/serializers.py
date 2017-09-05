from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class GeoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Geo
    fields = ('url',
              'pk', 
              'lat', 
              'lng')

class AddressSerializer(serializers.ModelSerializer):
  geo = GeoSerializer
  class Meta:
    model = Address
    fields = ('url',
              'pk', 
              'street', 
              'suite', 
              'city', 
              'zipcode')

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ('url',
              'pk',
              'name',
              'catchPhrase',
              'bs')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = ('url',
              'pk',
              'name', 
              'email', 
              'body', 
              'post')

class PostSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.SlugRelatedField(read_only=True,slug_field='username')
  comments = CommentSerializer(many=True, read_only=True)

  class Meta:
    model = Post
    fields = ('url',
              'pk',
              'title', 
              'body', 
              'owner',
              'comments')

class UserExtSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserExt
    fields = ('address',
              'company',
              'phone',
              'website')

class UserSerializer(serializers.HyperlinkedModelSerializer):
  posts = PostSerializer(many=True, read_only=True)
  userExt = UserExtSerializer(read_only=True)

  class Meta:
    model = User
    fields = ('url',
              'pk',
              'username',
              'userExt',
              'posts')

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = UserExt
#     fields = ('url',
#               'pk', 
#               'username',
#               'email',
#               'address',
#               'website',
#               'company')
