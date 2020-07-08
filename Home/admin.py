from django.contrib import admin
from .models import *


class BookmarkModel(admin.ModelAdmin):
    list_display = ('User', 'date_created')
    search_fields = ('User', 'date_created')

admin.site.register(Bookmark, BookmarkModel)



class BookmarkItemModel(admin.ModelAdmin):
    list_display = ('Bookmark_Owner', 'product_name', 'date_added')
    search_fields = ('Bookmark_Owner', 'product_name', 'date_added')

admin.site.register(BookmarkItem, BookmarkItemModel)