from rest_framework import filters

from django_filters import MethodFilter

from boxing.api import models

class ItemFilterSet(filters.FilterSet):

    related = MethodFilter()

    def filter_related(self, queryset, value):
        return queryset.filter(related__item=value)

    class Meta:
        model = models.Item
        fields = ('container', 'category')

class LendingFilterSet(filters.FilterSet):

    class Meta:
        model = models.Lending
        fields = ('id', 'state', 'account', 'item')

class MediaFilterSet(filters.FilterSet):

    class Meta:
        model = models.Media
        fields = ('item', )
