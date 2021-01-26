# importing django routing libraries 
from . import views 
from django.urls import path, include 
from .views import *
  
urlpatterns = [ 
    # home page 
    path('', views.bloglist.as_view(), name='blogs'), 
    path('<blog>/', views.postslist.as_view(), name='posts'), 
    path('<blog>/create-post', views.create_Post, name='create_post'),  
    # route for posts 
    path('<blog>/post/<slug:slug>', views.postdetail.as_view(), name='post_detail'),
    path('<blog>/post/<slug:slug>/upvote', views.upvote, name='upvote'),
    path('create-blog', views.create_blog, name='create_blog'),  
] 