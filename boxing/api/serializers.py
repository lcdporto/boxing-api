from rest_framework import serializers
from boxing.api import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'email', 'first_name', 'last_name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'created', 'updated')

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Container
        fields = ('id', 'name', 'created', 'updated')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ('id', 'name', 'image', 'container', 'category', 'quantity', 'created', 'updated')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Media
        fields = ('id', 'path', 'created', 'updated')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ('id', 'name', 'path', 'created', 'updated')
