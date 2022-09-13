from django.contrib.sites.models import Site
from django.db import models

class ImageForGroup(models.Model):
    pass

class Group(models.Model):
    site = models.ForeignKey(Site, blank=True, on_delete=models.CASCADE)
    pass

class Brand(models.Model):
    site = models.ForeignKey(Site, blank=True, on_delete=models.CASCADE)
    pass

class CarModel(models.Model):
    pass

class Vehicle(models.Model):
    pass

class Service(models.Model):
    pass

