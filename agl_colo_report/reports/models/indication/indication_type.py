from django.db import models

class IndicationTypeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class IndicationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    objects = IndicationTypeManager()
    
    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name,)

    class Meta:
        verbose_name = 'Indication Type'
        verbose_name_plural = 'Indication Types'
        ordering = ['name']
