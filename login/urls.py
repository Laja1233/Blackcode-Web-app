from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.handlelogin, name='handlelogin'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('terms', views.terms, name='terms'),


    
]