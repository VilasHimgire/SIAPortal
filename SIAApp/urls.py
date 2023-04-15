# from django.contrib import admin
# from django.urls import path, include
# from SIAApp import views

# urlpatterns = [
#     path('', views.index),
#     path('notes', views.notes),
#     path("assignment", views.assignment),
#     path('register',views.register),
#     path('login',views.loginUser),
#     path('logout',views.logoutUser),
# ]

# myproject/urls.py
from django.urls import path
from SIAApp import views

urlpatterns = [
    path('register', views.register,),
]
