from rest_framework import serializers
from boxing.api.models import *

class BoxSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Box
		fields = ('url', 'id', 'name', 'created', 'updated')

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Container
                fields = ('url', 'id', 'name', 'created', 'updated')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Item
                fields = ('url', 'id', 'name', 'box', 'created', 'updated')
