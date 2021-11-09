from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Languages)

class LanguageAdmin(admin.ModelAdmin):
    list_display=['name','code','icon','directory']
