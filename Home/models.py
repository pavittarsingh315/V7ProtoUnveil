from django.db import models
from django.utils import timezone
from Users.models import SiteUser
from Search.models import Product


class Bookmark(models.Model):
    User = models.OneToOneField(SiteUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User}'s Bookmarks"



class BookmarkItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200, default=None, null=True, blank=True)
    Bookmark = models.ForeignKey(Bookmark, on_delete=models.SET_NULL, null=True)
    Bookmark_Owner = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}"