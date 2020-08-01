from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.http import JsonResponse
import json
from .filters import BookmarkFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Advertisements import models as Ad_models
from Search import models as Search_models


def Error_404_custom(request, exception):
    return render(request, 'Home/404.html')


def home(request):
    order_qs = Search_models.Search.objects.order_by('-Frequency')[:10]
    context = {
        'tier1s': Ad_models.Tier1.objects.all(),
        'topten': order_qs,
    }
    return render(request, 'Home/homepage.html', context)


def donations(request):
    return render(request, 'Home/donations.html')

def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        # customer = stripe.Customer.create(
        #     email=request.POST['email'],
        #     name=request.POST['nickname'],
        #     source=request.POST['stripeToken'],
        # )
        #
        # charge = stripe.Charge.create(
        #     customer=customer,
        #     amount=amount*100,
        #     currency='usd',
        #     description='Donation'
        # )

    return redirect(reverse('donationsuccess', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'Home/donationsuccess.html', {'amount': amount})


def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    user = request.user
    product = models.Product.objects.get(id=productId)
    bookmark, created = models.Bookmark.objects.get_or_create(User=user)

    if action == 'add':
        models.BookmarkItem.objects.get_or_create(Bookmark=bookmark, product=product, Bookmark_Owner=user, product_name=product)
    elif action == 'remove':
        models.BookmarkItem.objects.filter(Bookmark=bookmark, product=product, Bookmark_Owner=user).delete()

    return JsonResponse('Item was added!', safe=False)


def bookmarks(request):
    user = request.user
    bookmarks = models.BookmarkItem.objects.filter(Bookmark_Owner=user).all()

    # i am a fucking god 06-24-20 8:13:30 pm

    myFilter = BookmarkFilter(request.GET, queryset=bookmarks)
    bookmarks = myFilter.qs

    bookmark_list = bookmarks.order_by('-date_added')
    page = request.GET.get('page', 1)

    paginator = Paginator(bookmark_list, 21)
    try:
        Bookmark = paginator.page(page)
    except PageNotAnInteger:
        Bookmark = paginator.page(1)
    except EmptyPage:
        Bookmark = paginator.page(paginator.num_pages)

    context = {
        'Bookmarks': Bookmark,
    }

    return render(request, 'Home/bookmarks.html', context)