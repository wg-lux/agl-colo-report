from django.db import models
from ..pathology_type import PathologyType

class SizeClassificationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class SizeClassification(models.Model):
    objects = SizeClassificationManager()
    
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)

    pathology_types = models.ManyToManyField(
        PathologyType,
        related_name='size_classifications',
        blank=True,
    )

    def __str__(self):
        return self.name_en
    
    def natural_key(self):
        return (self.name,)
