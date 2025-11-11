from django.contrib import admin
from django.urls import path, include
from django.urls import path
from front import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
    path('', views.index, name='index')
]
