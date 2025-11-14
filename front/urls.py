from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_ong/', views.registrar_ong, name='registrar_ong'),
]

urlpatterns = [
    path("", views.index, name="index"),
    path("registrar_ong/", views.registrar_ong, name="registrar_ong"),
    path("parceiros/", views.parceiros, name="parceiros"),
]
