from django.contrib import admin

from boxing.api import models

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'container', 'category', 'quantity')
    list_filter = ('container', 'category', 'quantity')
    search_fields = ('name', )

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Container)
admin.site.register(models.Category)
