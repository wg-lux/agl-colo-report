from django.db import models

class InterventionTypeManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class InterventionType(models.Model):
    objects = InterventionTypeManager()

    name = models.CharField(max_length=255, unique=True)  # natural key
    name_de = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    pathology_types = models.ManyToManyField('PathologyType', related_name='intervention_types')
    description = models.TextField()

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class InterventionManager(models.Model):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Intervention(models.Model):
    objects = InterventionManager()

    name = models.CharField(max_length=255, unique=True)  # natural key
    name_de = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField()
    pathology_types = models.ManyToManyField(
        'PathologyType', related_name='interventions'
    )
    intervention_types = models.ManyToManyField(
        InterventionType, related_name='interventions'
    )
    # instruments and complication fields will be added later