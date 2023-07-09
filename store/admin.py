import sys
from django.contrib import admin

from mechanic_api.settings import BASE_DIR

from .models import Customer, Vehicle, VehicleCategory

from django.utils.html import format_html

from django.contrib.sites.shortcuts import get_current_site



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user_id', 'phone_number', 'first_name',
                    'last_name', 'description']
    autocomplete_fields = ['user']
    search_fields = ['user__first_name', 'user__last_name']



@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'category', 'type', 'image']
    list_display = ['id', 'name', 'category', 'type', 'thumbnail']
    # readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            # print(instance.image.url)
            # sys.exit()
            return format_html(f'<img src= "{instance.image.url}" class="thumbnail"/>')
        return ''

    