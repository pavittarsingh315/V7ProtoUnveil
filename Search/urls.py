from django.urls import path

from . import views
# s
urlpatterns = [
    path('', views.search, name='searchpage'),
]