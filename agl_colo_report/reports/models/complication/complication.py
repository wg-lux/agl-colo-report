from django.db import models

class ComplicationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Complication(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    complication_types = models.ManyToManyField('ComplicationType', blank=True)
    objects = ComplicationManager()

    def __str__(self):
        return self.name
    
    def natural_key(self):
        return (self.name,)

    class Meta:
        verbose_name = 'Complication'
        verbose_name_plural = 'Complications'
        ordering = ['name']
