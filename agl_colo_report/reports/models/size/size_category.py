from django.db import models
from ..shared.unit import Unit
from .size_classification import SizeClassification

class SizeCategoryManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    

class SizeCategory(models.Model):
    objects = SizeCategoryManager()

    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    size_min = models.FloatField(null=True, blank=True)
    size_max = models.FloatField(null=True, blank=True)
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    classification = models.ForeignKey(
        SizeClassification,
        on_delete=models.CASCADE,
        related_name='size_categories',
        null=True,
        blank=True,
    )
    
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name_en
    
    def natural_key(self):
        return (self.name,)