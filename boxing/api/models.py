import os

from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings

from boxing.api import mixins

class AccountManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):

        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        # create a normal user account
        account = self.create_user(email, password, **kwargs)
        # set this new user as a superuser
        account.is_superuser = True
        account.save()
        return account

# here we are extending the default user model
class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # i'm adding this because i'm trying to use the admin interface
    is_staff = models.BooleanField(default=False)
    # auto_now_add automatically sets the field to now on object creation
    created = models.DateTimeField(auto_now_add=True)
    # auto_now automatically sets the field to now every time the object is saved
    updated = models.DateTimeField(auto_now=True)
    objects = AccountManager()

    def full_name(self):
        return self.get_full_name();

    # we will use the email as the username credential
    # the required field here is need because it's the way
    # django wants it when extending the default model (?)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # string representation of the account object
    def __unicode__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name])
        else:
            return None

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        else:
            return None

    def has_perm(self, perm, obj=None):
        return self.is_admin()

    def has_module_perms(self, app_label):
        return self.is_admin()

    # for a user to be an admin it has to fulfil 3 conditions, active, superuser and staff
    def is_admin(self):
        return self.is_superuser and self.is_staff and self.is_active

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Container(models.Model):
    name = models.CharField(max_length=1024, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Item(mixins.Timestampable, models.Model):
    name = models.CharField(max_length=1024, null=False)
    container = models.ForeignKey('Container', null=True)
    category = models.ForeignKey('Category', null=True)
    avatar = models.CharField(max_length=100, default=settings.DEFAULT_MEDIA['ITEM_AVATAR'])
    quantity = models.SmallIntegerField(null=True, default=None)
    documentation = models.URLField(null=True)

    def __str__(self):
        return self.name

class Media(mixins.Timestampable, models.Model):
    """
    Media Model
    """
    path = models.FileField(max_length=100, upload_to='%Y/%m/%d/')
    item = models.ForeignKey('Item', null=True)

class Photo(models.Model):
    name = models.CharField(max_length=255, null=True)
    path = models.ImageField(null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

class Related(mixins.Timestampable, models.Model):
    item = models.ForeignKey('Item', related_name='item')
    related = models.ForeignKey('Item', related_name='related')
