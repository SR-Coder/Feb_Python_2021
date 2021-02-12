from django.shortcuts import render, HttpResponse

# Create your views here.
def displayIndex(request):
    return HttpResponse('hello world')