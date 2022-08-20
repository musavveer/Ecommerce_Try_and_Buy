from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("profile", views.profile, name='profile'),
    path("contact", views.contact, name='contact'),

    path('add/', views.addPhoto, name="add"),
    path('product1', views.product1, name="product1"),
    path('product2', views.product2, name="product2"),
    path('product3', views.product3, name="product3"),
    path('product4', views.product4, name="product4"),
    path('product5', views.product5, name="product5"),
    path('product6', views.product6, name="product6"),

] 
 