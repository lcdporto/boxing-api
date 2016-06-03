from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response

from boxing.api.serializers import *
from boxing.api.models import *
from boxing.api import filtersets

class AccountViewSet(viewsets.ModelViewSet):
    """
    A list of users
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @list_route(permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

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
    ordering_fields = ('name',)
    ordering = 'name'

class ItemViewSet(viewsets.ModelViewSet):
    """
    A list of items
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_class = filtersets.ItemFilterSet
    search_fields = ('name', )

class MediaViewSet(viewsets.ModelViewSet):
    """
    A list of media items
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]

class PhotoViewSet(viewsets.ModelViewSet):
    """
    A list of photos
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]
