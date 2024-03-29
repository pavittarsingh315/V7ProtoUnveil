from django.db import models
from django.utils import timezone


class User_Search(models.Model):
    Search_value = models.CharField(max_length=100, null=True)
    Search_User = models.CharField(max_length=200, default=None, null=True, blank=True)
    Frequency = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return '{}'.format(self.Search_value)

    def save(self, *args, **kwargs):
        for field_name in ['Search_value']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(User_Search, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "User Searches"

class Search(models.Model):
    Search_value = models.CharField(max_length=100, null=True)
    Frequency = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return '{}'.format(self.Search_value)

    def save(self, *args, **kwargs):
        for field_name in ['Search_value']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Search, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Searches"


class Product(models.Model):
    Search = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=10, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Link = models.CharField(max_length=300, null=True, blank=True)
    Image = models.CharField(max_length=300, null=True, blank=True)
    Seller = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.Name)


    class Meta:
        verbose_name_plural = "Products"