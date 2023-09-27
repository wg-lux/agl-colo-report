from django.db import models
from .organ import Organ

class OrganComponentManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class OrganComponent(models.Model):
    objects = OrganComponentManager()

    organ = models.ForeignKey(
        Organ,
        on_delete=models.CASCADE,
        related_name="components",
        )
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    component_order_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.organ.name_en} - {self.name_en}"

    def natural_key(self):
        return (self.name,)