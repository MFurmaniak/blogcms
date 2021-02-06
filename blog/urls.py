# importing django routing libraries 
from . import views 
from django.urls import path, include 
from .views import *
  
urlpatterns = [ 

    path('', views.bloglist.as_view(), name='blogs'),
    path('create-blog', views.create_blog, name='create_blog'),   
    path('edit', views.editbloglist.as_view(), name='edit'),   
    path('edit/edit/<slug:slug>', views.blogEditView.as_view(), name='edit_blog'),  
    path('edit/delete/<slug:slug>', views.blogDeleteView.as_view(), name='deleteblog'),
    path('edit/<blog>/create-post', views.create_Post, name='create_post'),  
    path('edit/<blog>/', views.postseditlist.as_view(), name='postseditlist'),  
    path('edit/<blog>/delete/<slug:slug>', views.postDeleteView.as_view(), name='deletepost'), 
    path('edit/<blog>/<slug:slug>', views.postEditView.as_view(), name='editpost'),   
    path('<blog>/', views.postslist.as_view(), name='posts'), 
    path('<blog>/post/<slug:slug>', views.postdetail.as_view(), name='post_detail'),
    path('<blog>/post/<post>/delete/<pk>', views.deletecommentView.as_view(), name='deletecom'),
    path('<blog>/post/<slug:slug>/upvote', views.upvote, name='upvote'),
] 