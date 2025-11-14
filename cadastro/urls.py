from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_ong/', views.registrar_ong, name='registrar_ong'),
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
    path("ongs/aprovadas/", views.ongs_aprovadas, name="ongs_aprovadas"),
]


urlpatterns = [
    path("parceiros/", views.parceiros, name="parceiros"),
]
