from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class Container(models.Model):
    name = models.CharField(max_length=1024, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

class Item(models.Model):
    name = models.CharField(max_length=1024, null=False)
    container = models.ForeignKey('Container')
    category = models.ForeignKey('Category', null=True)
    image = models.CharField(max_length=255)
    quantity = models.SmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated= models.DateTimeField(auto_now=True, null=False)
