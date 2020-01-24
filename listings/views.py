from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'listings/search.html')