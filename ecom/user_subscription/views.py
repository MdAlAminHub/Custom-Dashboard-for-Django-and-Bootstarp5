from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'user_subscription/index.html')
