from django.shortcuts import render
from django.http import HttpResponse
# get Listing model
from listings.models import Listing
# get Realtor model
from realtors.models import Realtor

def index(request):
    # [:3] means limit to 3 listings
    listings = Listing.objects.order_by('-id').filter(is_published=True)[:3]
    data = {
        'listings': listings
    }
    return render(request, 'pages/index.html', data)

def about(request):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # get mvp realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    data = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', data)

