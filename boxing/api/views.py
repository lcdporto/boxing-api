# django-rest-framework imports
from rest_framework import viewsets
from rest_framework import filters
#
from boxing.api.serializers import *
from boxing.api.models import *

class AccountViewSet(viewsets.ModelViewSet):
    """
    A list of users
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A list of categories to categorize items
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContainerViewSet(viewsets.ModelViewSet):
    """
    A list of containers
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)

class ItemViewSet(viewsets.ModelViewSet):
    """
    A list of items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    """
    A list of photos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
