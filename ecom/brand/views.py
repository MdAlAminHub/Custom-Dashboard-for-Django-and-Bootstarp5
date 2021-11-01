from django.shortcuts import render
from .serializers import *
from .models import *

def index(request):
    return render(request, 'brand/index.html')
