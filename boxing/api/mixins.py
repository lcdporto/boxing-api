from django.db import models

class Timestampable(models.Model):
    """
    Adds created and updated fields
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
