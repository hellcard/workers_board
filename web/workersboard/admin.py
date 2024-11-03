from django.contrib import admin

from .models import Workers as ws
# Register your models here.

class Wba(admin.ModelAdmin):
    list_display = ('name','age','exp')
    list_display_links = ('name','age')
    search_fields = ('age','exp')

admin.site.register(ws,Wba)