from django.contrib import admin
from .models import Nout
# Register your models here.

@admin.register(Nout)
class NoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']