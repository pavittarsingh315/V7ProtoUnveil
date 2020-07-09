from django.urls import path

from . import views
from Users.decorators import unauthenticated_user

urlpatterns = [
    path('', views.home, name='homepage'),
    path('bookmarks/', unauthenticated_user(views.bookmarks), name='bookmarks'),
    path('update_item/', views.UpdateItem, name='update_item'),
]