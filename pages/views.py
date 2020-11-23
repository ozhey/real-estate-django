from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtor = realtors.filter(is_mvp=True).first()

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }

    return render(request, 'pages/about.html', context)
