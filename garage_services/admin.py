from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service, Group, Brand, CarModel, Vehicle, ServicesVehicle, Engine, Transmission, Drive, Lead, ImageDesing

class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'content',
        )

class GroupAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        )

class BrandAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        )

class CarModelAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        )

class VehicleAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        )

class ImageDesingAdmin():
    # TODO: отображение в админке
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(ServicesVehicle)
admin.site.register(Engine)
admin.site.register(Transmission)
admin.site.register(Drive)
admin.site.register(Lead)
admin.site.register(ImageDesing)