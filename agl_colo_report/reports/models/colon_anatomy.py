from django.db import models
from .organ_component import OrganComponent
from .anastomosis import Anastomosis

class ColonAnatomyManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class ColonAnatomy(models.Model):
    objects = ColonAnatomyManager()
    
    available_segments = models.ManyToManyField(
        OrganComponent, 
        related_name='available_in_anatomies'
        )
    available_anastomoses = models.ManyToManyField(
        Anastomosis, 
        related_name='available_in_anatomies', 
    blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Anatomy"
    
    def natural_key(self):
        return (self.name,)
    
    def get_available_segments_ordered(self):
        """Returns the available segments ordered by component_order_id (descending))"""
        # "-" in front of component_order_id means descending order
        return self.available_segments.order_by('-component_order_id')