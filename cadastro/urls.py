from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_ong, name='registrar_ong'),
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),
]