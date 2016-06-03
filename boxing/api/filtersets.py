from rest_framework import filters

from boxing.api import models

class ItemFilterSet(filters.FilterSet):

    class Meta:
        model = models.Item
        fields = ('container', 'category')
