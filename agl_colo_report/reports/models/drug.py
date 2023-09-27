# models/drug_application.py

from django.db import models

class DrugManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Drug(models.Model):
    objects = DrugManager()

    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    preferred_unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.abbreviation
    
    def natural_key(self):
        return (self.name,)
