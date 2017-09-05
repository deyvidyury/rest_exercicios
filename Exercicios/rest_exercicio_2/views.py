from rest_exercicio_2.models import *
from rest_exercicio_2.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_exercicio_2.permissions import IsOwnerOrReadOnly, IsPostOwner
import json

#Users
class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-list'
  permission_classes = (
    permissions.IsAuthenticatedOrReadOnly
  )

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  name = 'user-detail'
  permission_classes = (
    permissions.IsAuthenticatedOrReadOnly
  )

# Posts
class PostList(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  name = 'post-detail'
  permission_classes = (
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly,
  )

# Comments
class CommentList(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  name = 'comment-detail'
  permission_classes = (
    permissions.IsAuthenticatedOrReadOnly,
    IsPostOwner,
  )

class ApiRoot(generics.GenericAPIView):
  name = 'api-root'
  def get(self, request, *args, **kwargs):
    return Response({
      'posts': reverse(PostList.name, request=request),
      'comments': reverse(CommentList.name, request=request),
      'users': reverse(UserList.name, request=request),
      })

# Import data from db.json
def import_users(request):
  dump_data = open('./db.json','r')
  as_json = json.load(dump_data)

  # Load user's information
  for user in as_json['users']:
    geo = Geo.objects.create(lat=user['address']['geo']['lat'],
                             lng=user['address']['geo']['lng'])

    adress = Addres.objects.create(street = user['address']['street'],
                                   suite = user['address']['suite'],
                                   city = user['address']['city'],
                                   zipcode = user['address']['zipcode'],
                                   geo = geo)

    company = Company.objects.create(name = user['company']['name'],
                                     catchPhrase = user['company']['catchPhrase'],
                                     bs = user['company']['bs'])

    User.objects.create(id = user['id'],
                        name = user['name'],
                        username = user['username'],
                        email = user['email'],
                        address = address,
                        phone = user['phone'],
                        website = user['website'],
                        company = company)
def import_posts(request):
  dump_data = open('db.json','r')
  as_json = json.load(dump_data)

  # Load Post's information
  for post in as_json['posts']:
    user = User.objects.get(id = post['user_Id'])
    Post.objects.create(id = post['id'],
                        title = post['title'],
                        body = post['body'],
                        user = user)

def import_comments(request):
  dump_data = open('db.json','r')
  as_json = json.load(dump_data)
  # Load Comment's information
  for comment in as_json['comments']:
    post = Post.objects.get(id = comment['post_Id'])
    Comment.objects.create(id = comment['id'],
                           name = comment['name'],
                           email = comment['email'],
                           body = comment['body'])