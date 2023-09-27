from django.db import models

class PathologyTypeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
    def get_by_natural_keys(self, *names):
        return self.filter(name__in=names)
    
class PathologyType(models.Model):
    objects = PathologyTypeManager()

    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
