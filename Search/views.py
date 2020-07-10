from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .scraping import final_product, walmart, hollister

final_product = final_product

def search(request):
    search = request.POST.get('search')

    walmart(request)
    hollister(request)


    product_list = sorted(final_product)
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 12)
    try:
        Products = paginator.page(page)
    except PageNotAnInteger:
        Products = paginator.page(1)
    except EmptyPage:
        Products = paginator.page(paginator.num_pages)

    stuff_for_frontend = {
        'Search': search,
        'products': Products,
    }
    # 07/8/20 11:56 pm
    return render(request, 'Search/search.html', stuff_for_frontend)

