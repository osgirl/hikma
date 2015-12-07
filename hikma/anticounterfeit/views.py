from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, State, City, Pharmacy, Doctor
from pip._vendor.requests.models import Response


# Create your views here.
def index(request):
    response = "AntiCounterFeit Home Page"
    return HttpResponse(response)

def check(request):
    return render(request, 'anticounterfeit/check.html',)
'''
def checkCSS(request):
    return render(request, 'anticounterfeit/check.css',)
'''
def state(request):
    states = get_list_or_404(State.objects.all())
    return render(request, 'anticounterfeit/state', {'states': states})

def city(request, state):
    response = "Nasr City, ALMohandsein,  ..."
    return HttpResponse(response)