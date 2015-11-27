from rest_framework import serializers
from boxing.api.models import *

class AccountSerializer(serializers.ModelSerializer):
        class Meta:
                model = Account
                fields = ('id', 'email', 'first_name', 'last_name')

class CategorySerializer(serializers.ModelSerializer):
        class Meta:
                model = Category
                fields = ('id', 'name', 'created', 'updated')

class ContainerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Container
                fields = ('id', 'name', 'created', 'updated')

class ItemSerializer(serializers.ModelSerializer):
        class Meta:
                model = Item
                fields = ('id', 'name', 'image', 'container', 'category', 'quantity', 'created', 'updated')
