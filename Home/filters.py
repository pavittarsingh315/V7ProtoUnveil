import django_filters
from django_filters import CharFilter

from .models import *

class BookmarkFilter(django_filters.FilterSet):
    product_name = CharFilter(field_name='product_name', lookup_expr='icontains')
    class Meta:
        model = BookmarkItem
        fields = '__all__'
        exclude = ['date_added', 'Bookmark_Owner', 'Bookmark', 'product', 'product_name']