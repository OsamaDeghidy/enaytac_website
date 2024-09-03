from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.mainview , name='mainview'),

    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('contactus/', views.contactus, name='contactus'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),

]
