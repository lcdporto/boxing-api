from rest_framework import serializers

from boxing.api import models
from boxing.api import validators

class CreateOnlyCurrentUserDefault(object):
    """
    Fetches the value of the current request user
    and returns it, to be used in field with a default
    value, only passes the request user if the resource
    is being created, after that returns the member field
    on the resource
    """
    def set_update_user_value(self, serializer_field):
        self.is_update = serializer_field.parent.instance is not None
        if self.is_update:
            self.initial_value = serializer_field.parent.instance.account

    def set_context(self, serializer_field):
        self.set_update_user_value(serializer_field)
        self.user = serializer_field.context['request'].user

    def __call__(self):
        if not self.is_update:
            return self.user
        return self.initial_value

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

class LendingSerializer(serializers.ModelSerializer):

    account = serializers.PrimaryKeyRelatedField(
            read_only=True, default=CreateOnlyCurrentUserDefault())

    start_date = serializers.DateTimeField(allow_null=False, required=True)
    end_date = serializers.DateTimeField(allow_null=False, required=True)

    def __init__(self, *args, **kwargs):
        override_read_only_fields = kwargs.pop('override_read_only_fields', None)
        super(LendingSerializer, self).__init__(*args, **kwargs)
        if override_read_only_fields:
            for field in override_read_only_fields:
                    self.fields[field].read_only = False

    class Meta:
        model = models.Lending
        fields = ('id', 'account', 'item', 'start_date', 'end_date', 'return_date', 'state',
                  'lending_reason', 'refusal_reason', 'notes', 'created', 'updated')
        read_only_fields = ('account', 'return_date', 'state')

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
