from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .scraping import *
from Advertisements import models as Ad_models
from itertools import chain
from operator import attrgetter

def search(request):
    search = request.POST.get('search').capitalize()

    if models.Product.objects.filter(Search=search):
        searchcreateobject(request)

        product_list = models.Product.objects.filter(Search=search).all().order_by('Name')
        # ads = Ad_models.SearchPageAds.objects.filter(Keywords=search).all()
        # product_list = sorted(chain(products, ads), key=attrgetter('Name'))
    else:
        searchcreateobject(request)

        Walmart(request)
        Hollister(request)
        Abercrombie(request)
        CostCo(request)
        HomeDepot(request)
        SamsClub(request)

        product_list = models.Product.objects.filter(Search=search).all().order_by('Name')
        # ads = Ad_models.SearchPageAds.objects.filter(Keywords=search).all()
        # product_list = sorted(chain(products, ads), key=attrgetter('Name')) eating hajmola

    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(product_list, 3)
    # try:
    #     Products = paginator.page(page)
    # except PageNotAnInteger:
    #     Products = paginator.page(1)
    # except EmptyPage:
    #     Products = paginator.page(paginator.num_pages)

    stuff_for_frontend = {
        'Search': search,
        'products': product_list,
        'tier2s': Ad_models.Tier2.objects.filter(Keywords=search).all(),
        'searchads': Ad_models.SearchPageAds.objects.filter(Keywords=search).all(),
    }
    return render(request, 'Search/search.html', stuff_for_frontend)

