from rest_framework import viewsets
from boxing.api.serializers import *
from boxing.api.models import *

class ContainerViewSet(viewsets.ModelViewSet):
    """
    A list of containers
    """
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    A list of items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    
