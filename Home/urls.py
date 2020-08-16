from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('update_item/', views.UpdateItem, name='update_item'),

    path('donations/', views.donations, name="donations"),
    path('donationdata/', views.donationcomplete, name="donationdata"),
    path('donationsuccess/', views.successMsg, name="donationsuccessful"),
]