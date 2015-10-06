from django.db import models

class Box(models.Model):
    name = models.CharField(max_length=1024, null=False)
    container = models.ForeignKey('Container')
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class Container(models.Model):
    name = models.CharField(max_length=1024, null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

class Item(models.Model):
    name = models.CharField(max_length=1024, null=False)
    box = models.ForeignKey('Box')
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated= models.DateTimeField(auto_now=True, null=False)
