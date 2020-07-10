from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .scraping import walmart, hollister

def search(request):
    search = request.POST.get('search')

    walmart(request)
    hollister(request)

    product_list = models.Product.objects.get_queryset().order_by('Name')
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
    return render(request, 'Search/search.html', stuff_for_frontend)

