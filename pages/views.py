from django.shortcuts import render
from django.http import HttpResponse
# get Listing model
from listings.models import Listing
# get Realtor model
from realtors.models import Realtor
# get the search fields from choices file
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    # [:3] means limit to 3 listings
    listings = Listing.objects.order_by('-id').filter(is_published=True)[:3]
    data = {
        'listings': listings,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
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

