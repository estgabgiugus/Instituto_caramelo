from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ONG


@admin.register(ONG)
class ONGAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "representante", "cnpj")
