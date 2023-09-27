from django.db import models
from .indication_type import IndicationType

class IndicationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class Indication(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    indication_types = models.ManyToManyField(IndicationType, blank=True)
    objects = IndicationManager()
    
    def natural_key(self):
        return (self.name,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Indication'
        verbose_name_plural = 'Indications'
        ordering = ['name']