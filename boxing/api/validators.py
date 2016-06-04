from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from rest_framework import serializers

import boxing.api.models

class MediaValidator(object):
    """
    Validates if a string passed to a field
    accepting media resources is in fact a media
    resource
    """

    message = 'This field must be a valid media resource.'

    def __call__(self, value):
        if value in settings.DEFAULT_MEDIA.values():
            return
        try:
            boxing.api.models.Media.objects.get(path=value)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(self.message)
