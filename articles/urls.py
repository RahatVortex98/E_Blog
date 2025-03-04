
from django.urls import path

from .import views

urlpatterns = [
    path('articles/', views.article_list,name='article_list'),
    path('create/', views.create_article,name='create_article'),
  
    path('articles/<slug:slug>/', views.article_details,name='article_details'),
    
]
