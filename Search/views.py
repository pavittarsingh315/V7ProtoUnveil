from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .scraping import walmart, hollister, searchcreateobject

def search(request):
    search = request.POST.get('search')

    if models.Product.objects.filter(Search=search):
        product_list = models.Product.objects.filter(Search=search).all().order_by('Name')
        searchcreateobject(request)
    else:
        searchcreateobject(request)
        walmart(request)
        hollister(request)

        product_list = models.Product.objects.filter(Search=search).all().order_by('Name')

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
    }
    return render(request, 'Search/search.html', stuff_for_frontend)

