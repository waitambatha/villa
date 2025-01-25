from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

   path("", views.index, name='index'),
   path('contact',views.contact , name='contact'),
path('properties',views.properties , name='properties'),
path('property_details',views.property_details , name='property_details')


]
