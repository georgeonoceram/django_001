from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html')