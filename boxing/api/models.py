from django.db import models

class Container(models.Model):
    name = models.CharField(max_length=1024, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class Item(models.Model):
    name = models.CharField(max_length=1024, null=False)
    container = models.ForeignKey('Container')
    image = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated= models.DateTimeField(auto_now=True, null=False)
