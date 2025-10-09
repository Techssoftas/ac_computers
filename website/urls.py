from django.contrib import admin
from django.urls import path,include
from website.views import *
urlpatterns = [
   
  path('',index,name='index'),  # Include the URLs from the website app
  path('about/',about,name='about'),  # Include the URLs from the website app
  path('contact/',contact,name='contact'),  # Include the URLs from the website app
  
]