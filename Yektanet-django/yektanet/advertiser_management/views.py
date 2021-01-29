from django.http import HttpResponse
from django.shortcuts import render

def ads_index(request):
    #we should return the given template and inc views
    return HttpResponse("it works")

