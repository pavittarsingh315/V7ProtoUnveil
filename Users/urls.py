from django.urls import path
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from . import views

urlpatterns = [
    path('register/', unauthenticated_user(views.register), name='registerpage'),
    path('profile/', login_required(views.profile), name='profilepage'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]