from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Hello, welcome to the index page!")
# Create your views here.
