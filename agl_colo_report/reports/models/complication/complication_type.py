from django.db import models

class ComplicationTypeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ComplicationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    objects = ComplicationTypeManager()

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name,)

    class Meta:
        verbose_name = 'Complication Type'
        verbose_name_plural = 'Complication Types'
        ordering = ['name']
