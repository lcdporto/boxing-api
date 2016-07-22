from django.contrib import admin

from boxing.api import models


def set_undefined_quantity(modeladmin, request, queryset):
    queryset.update(quantity=None)
set_undefined_quantity.short_description = "Set Items Quantity to Undefined"

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'container', 'category', 'quantity')
    list_filter = ('container', 'category', 'quantity')
    search_fields = ('name', )
    actions = [set_undefined_quantity]

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Container)
admin.site.register(models.Category)
