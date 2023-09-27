from django.db import models


class OrganManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Organ(models.Model):
    objects = OrganManager()

    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    components_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
    
