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

def checkQRCode(request, QRCode):
    return render(request, 'anticounterfeit/check.html', {'QRCode': QRCode})

def product(request):
    products = Product.objects.all()
    return render(request, 'anticounterfeit/product', {'products': products})

def state(request):
    states = State.objects.all()
    return render(request, 'anticounterfeit/state', {'states': states})

def city(request, statePK):
    cities = City.objects.filter(state=statePK)
    return render(request, 'anticounterfeit/city', {'cities': cities})

def pharmacy(request, cityPK):
    pharmacies = Pharmacy.objects.filter(city=cityPK)
    return render(request, 'anticounterfeit/pharmacy', {'pharmacies': pharmacies})

def doctor(request, cityPK):
    doctors = Doctor.objects.filter(city=cityPK)
    return render(request, 'anticounterfeit/doctor', {'doctors': doctors})