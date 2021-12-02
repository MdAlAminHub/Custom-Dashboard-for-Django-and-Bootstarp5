from django.contrib import admin
from .models import Categories, SubCategories, SubCategories_2

# Register your models here.

admin.site.register(Categories)

admin.site.register(SubCategories)
admin.site.register(SubCategories_2)
