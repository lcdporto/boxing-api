from rest_framework import serializers
from boxing.api.models import *

class CategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Category
                fields = ('id', 'url', 'name', 'created', 'updated')

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Container
                fields = ('url', 'id', 'name', 'created', 'updated')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
        # display field for the browsable api, drf by default
        # uses __str__ method of model
        class RelatedModelDisplayField(serializers.PrimaryKeyRelatedField):
                def display_value(self, instance):
                        return instance.name
                
        category = RelatedModelDisplayField(queryset=Category.objects.all())
        container = RelatedModelDisplayField(queryset=Container.objects.all())
        
        class Meta:
                model = Item
                fields = ('url', 'id', 'name', 'image', 'container', 'category', 'quantity', 'created', 'updated')
