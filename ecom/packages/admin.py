from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Packages)

admin.site.register(PackagesType)
admin.site.register(PackagesTypeAttributes)
