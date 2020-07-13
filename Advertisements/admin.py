from django.contrib import admin
from .models import *

# 07-12-20 Im too good

class AdvertisementTier1(admin.ModelAdmin):
    list_display = ('company', 'payment', 'header', 'date_created')
    search_fields = ('company', 'header',)
    fieldsets = (
        ('Private', {'fields': ('company', 'payment',)}),
        ('Content', {'fields': ('header', 'image_url', 'redirect_url', 'front_content', 'hidden_content')}),
        ('General', {'fields': ('date_created',)})
    )

admin.site.register(Tier1, AdvertisementTier1)


class AdvertisementTier2(admin.ModelAdmin):
    list_display = ('company', 'payment', 'header', 'date_created')
    search_fields = ('company', 'header',)
    fieldsets = (
        ('Private', {'fields': ('company', 'payment',)}),
        ('Content', {'fields': ('symbol', 'symbol_hex_color', 'header', 'content')}),
        ('General', {'fields': ('date_created',)})
    )

admin.site.register(Tier2, AdvertisementTier2)


class LoadedSearchPage(admin.ModelAdmin):
    list_display = ('company', 'Seller', 'payment', 'Name', 'date_created')
    search_fields = ('company', 'Seller', 'Name', 'Price')
    fieldsets = (
        ('Private', {'fields': ('company', 'payment',)}),
        ('Content', {'fields': ('Seller', 'Name', 'Image', 'Link', 'Price', 'Description')}),
        ('General', {'fields': ('date_created',)})
    )

admin.site.register(SearchPageAds, LoadedSearchPage)
