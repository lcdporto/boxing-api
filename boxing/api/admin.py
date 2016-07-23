from django.contrib import admin

from boxing.api import models

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'container', 'category', 'quantity')
    list_filter = ('container', 'category', 'quantity')
    search_fields = ('name', )
    actions = ['set_undefined_quantity']

    def set_undefined_quantity(self, request, queryset):
        updated = queryset.update(quantity=None)
        self.message_user(request, "successfully set {0} items quantity to undefined.".format(updated))
    set_undefined_quantity.short_description = "Set Items Quantity to Undefined"

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Container)
admin.site.register(models.Category)
