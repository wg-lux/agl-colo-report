from django.db import models

class InstrumentManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class Instrument(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, unique=True)
    name_en = models.CharField(max_length=100, unique=True)
    instrument_types = models.ManyToManyField('InstrumentType', blank=True, related_name='instruments')
    objects = InstrumentManager()
    
    def natural_key(self):
        return (self.name,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Instrument'
        verbose_name_plural = 'Instruments'
        ordering = ['name']