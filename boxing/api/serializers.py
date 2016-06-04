from rest_framework import serializers

from boxing.api import models
from boxing.api import validators

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

    avatar = serializers.CharField(
            max_length=100,
            required=False,
            validators=[validators.MediaValidator()]
    )

    class Meta:
        model = models.Item
        fields = ('id', 'name', 'avatar', 'container', 'category', 'quantity', 'documentation',
                  'description', 'created', 'updated')

class MediaSerializer(serializers.ModelSerializer):

    path = serializers.FileField(
        max_length=100,
        allow_empty_file=False,
        use_url=False
    )
        
    class Meta:
        model = models.Media
        fields = ('id', 'path', 'item', 'created', 'updated')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ('id', 'name', 'path', 'created', 'updated')

class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Related
        fields = ('id', 'item', 'related', 'created', 'updated')
