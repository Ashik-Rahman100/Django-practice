from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def fees_dj(request):
    return HttpResponse('300')

def fees_py(request):
    return HttpResponse('200')
