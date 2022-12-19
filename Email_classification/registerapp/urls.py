from django.contrib import admin
from django.urls import path, include
from registerapp import views
urlpatterns = [
    # create online page urls='home' name when use database then it call name=home
    path('', views.home, name='home'),
    path('emailCheck/', views.EmailClassification),
]
