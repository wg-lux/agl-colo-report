from django.db import models

class InstrumentTypeManagement(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class InstrumentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    objects = InstrumentTypeManagement()
    
    def natural_key(self):
        return (self.name,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Instrument Type'
        verbose_name_plural = 'Instrument Types'
        ordering = ['name']
