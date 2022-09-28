from django.contrib import admin
from .models import Service, Group, Brand, CarModel, Vehicle, ServicesVehicle, Engine, Transmission, Drive, Lead, ImageDesing

# Register your models here.

admin.site.register(Service)
admin.site.register(Group)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Vehicle)
admin.site.register(ServicesVehicle)
admin.site.register(Engine)
admin.site.register(Transmission)
admin.site.register(Drive)
admin.site.register(Lead)
admin.site.register(ImageDesing)