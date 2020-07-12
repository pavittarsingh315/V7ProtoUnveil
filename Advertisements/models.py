from django.db import models
from django.utils import timezone



class Tier1(models.Model):
    company = models.CharField(max_length=100)
    payment = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    header = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=200, default=None)
    image_url = models.CharField(max_length=200, default=None)
    front_content = models.TextField()
    hidden_content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company


    class Meta:
        verbose_name_plural = "Homepage Ads"


class Tier2(models.Model):
    company = models.CharField(max_length=100)
    payment = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    header = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    symbol_hex_color = models.CharField(max_length=20, default=None)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Tier2"

class SearchPageAds(models.Model):
    company = models.CharField(max_length=100)
    payment = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    header = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=200, default=None)
    image_url = models.CharField(max_length=200, default=None)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=None)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = "Loaded Search Page Ads"
