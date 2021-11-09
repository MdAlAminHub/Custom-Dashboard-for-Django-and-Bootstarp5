from django.contrib import admin
from .models import *

# Register your models here.
class PagesModel(admin.ModelAdmin):
    list_display = ['page_slug', 'page_name_english',
                    'description_english', 'page_name_bangla']


admin.site.register(Pages, PagesModel)


