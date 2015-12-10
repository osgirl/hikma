from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from .models import Product, State, City, Pharmacy, Doctor
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie # to force setting of csrf cookie if form added dynamically to the page - for example through jquery
def index(request):
    response = "AntiCounterFeit Home Page"
    return HttpResponse(response)

def check(request):
    #c = {}
    #c.update(csrf(request))
    #return render_to_response('anticounterfeit/check.html', c)
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

@ensure_csrf_cookie  # to force setting of csrf cookie if form added dynamically to the page - for example through jquery
def result(request):
    product = request.POST.get('product', '')
    product = Product.objects.get(productPK=product)
    #c = {'product': product}
    #c.update(csrf(request))
    #return render_to_response('anticounterfeit/result.html', c)
    return render(request, 'anticounterfeit/result.html', {'product': product})