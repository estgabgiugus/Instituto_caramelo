from django.contrib import admin
from django.urls import path, include
from front import views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('front.urls')),
]
