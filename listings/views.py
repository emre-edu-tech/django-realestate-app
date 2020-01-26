from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# get the search fields from choices file
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    # fetch all listings from database
    # listings = Listing.objects.all()
    # fetch all listings and order them list_date or id descending
    listings = Listing.objects.order_by('-id').filter(is_published=True)
    # add pagination
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # prepare the objects as dictionaries to pass it to the view
    data = {
        'listings': paged_listings
    }
    # pass the dictionary to the view
    return render(request, 'listings/listings.html', data)

def listing(request, listing_id):
    # get the single listing using listing_id
    listing = get_object_or_404(Listing, pk=listing_id)
    data = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', data)

def search(request):
    # get all listings and assign it to a query set
    queryset_list = Listing.objects.order_by('-id')

    #### important note: if you want to search case insensitive use "i"
    # Check if any keyword is coming from the form
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Check if any city is coming from the form
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # queryset_list = queryset_list.filter(city__iexact=city)
            queryset_list = queryset_list.filter(city__icontains=city)
    
    # Check if any state is coming from the form
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Check if any bedrooms value is coming from the form
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(num_of_bedrooms__lte=bedrooms)
    
    # Check if any price value is coming from the form
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # send data to populate the search form
    data = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', data)