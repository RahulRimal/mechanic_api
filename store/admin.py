import sys
from django.contrib import admin

from mechanic_api.settings import BASE_DIR

from .models import Customer, Mechanic, Vehicle, VehicleCategory, VehiclePart, VehicleRepairRequest, VehicleRepairRequestImage, VehicleRepairRequestVideo

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
    
    


class VehiclePartAdminInline(admin.TabularInline):
    model = VehiclePart
    extra = 0
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            
            return format_html(f'<img class="thumbnail" src= "{instance.image.url}" class="thumbnail"/>')
        return ''
    class Media:
        css = {
            'all': ['store/style.css']
        }

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'category', 'image']
    list_display = ['id', 'name', 'category', 'thumbnail']
    # readonly_fields = ['thumbnail']
    inlines = [VehiclePartAdminInline]

    def thumbnail(self, instance):
        if instance.image.name != '':
            
            return format_html(f'<img class="thumbnail" src= "{instance.image.url}" class="thumbnail"/>')
        return ''
    class Media:
        css = {
            'all': ['store/style.css']
        }


@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    list_display = ['id','user_id', 'phone_number', 'first_name',
                    'last_name', 'description']
    autocomplete_fields = ['user']
    search_fields = ['user__first_name', 'user__last_name']
    


class VehicleRepairRequestImageAdminInline(admin.TabularInline):
    model = VehicleRepairRequestImage
    extra = 0
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            
            return format_html(f'<img class="thumbnail" src= "{instance.image.url}" class="thumbnail"/>')
        return ''
    class Media:
        css = {
            'all': ['store/style.css']
        }
class VehicleRepairRequestVideoAdminInline(admin.TabularInline):
    model = VehicleRepairRequestVideo
    extra = 0
    # readonly_fields = ['thumbnail']

    # def thumbnail(self, instance):
    #     if instance.image.name != '':
            
    #         return format_html(f'<img class="thumbnail" src= "{instance.image.url}" class="thumbnail"/>')
    #     return ''
    # class Media:
    #     css = {
    #         'all': ['store/style.css']
    #     }



@admin.register(VehicleRepairRequest)
class VehicleRepairRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','preferred_mechanic', 'location_name', 'location_coordinates', 'description', 'created_at']
    inlines = [VehicleRepairRequestImageAdminInline, VehicleRepairRequestVideoAdminInline]