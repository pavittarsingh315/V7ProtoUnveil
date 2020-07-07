from django.contrib import admin
from .models import *


class SearchAdmin(admin.ModelAdmin):
    list_display = ('Search_User', 'Search_value', 'date_added')
    search_fields = ('Search_User', 'Search_value')

admin.site.register(Search, SearchAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Seller')
    search_fields = ('Name', 'Seller')

admin.site.register(Product, ProductAdmin)