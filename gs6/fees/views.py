from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def fees_python(request):
    return HttpResponse('300')

def fees_django(request):
    return HttpResponse('200')
