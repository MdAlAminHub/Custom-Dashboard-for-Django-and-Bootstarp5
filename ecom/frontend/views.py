from django.shortcuts import render

# Create your views here.


def indexf(request):
    return render(request, 'frontend/index-1.html')
