from django.conf.urls import url
from rest_exercicio_2 import views

urlpatterns = [
  url(r'^users/$', 
    views.UserList.as_view(), 
    name=views.UserList.name),
  url(r'^users/(?P<pk>[0-9]+)/$',
    views.UserDetail.as_view(),
    name=views.UserDetail.name),

  url(r'^posts/$',
    views.PostList.as_view(),
    name=views.PostList.name),
  url(r'^posts/(?P<pk>[0-9]+)/$',
    views.PostDetail.as_view(),
    name=views.PostDetail.name),

  url(r'^comment/$',
    views.CommentList.as_view(),
    name=views.CommentList.name),
  url(r'^comment/(?P<pk>[0-9]+)/$',
    views.CommentDetail.as_view(),
    name=views.CommentDetail.name),
  
  url(r'^$',
    views.ApiRoot.as_view(),
    name=views.ApiRoot.name),

  url(r'^import_users/$', views.import_users),
  url(r'^import_posts/$', views.import_posts),
  url(r'^import_comments/$', views.import_comments),
]