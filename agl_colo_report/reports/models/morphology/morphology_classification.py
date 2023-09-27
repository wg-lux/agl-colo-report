from django.db import models

class MorphologyClassificationManager(models.Manager):   
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class MorphologyClassification(models.Model):
    objects = MorphologyClassificationManager()
    
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    pathology_types = models.ManyToManyField(
        'PathologyType',
        related_name='morphology_classifications',
        blank=True,
    )

    description = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name_en
    
    def natural_key(self):
        return (self.name,)
