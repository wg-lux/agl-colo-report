from django.db import models

class MorphologyCategoryManager(models.Manager):   
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class MorphologyCategory(models.Model):
    objects = MorphologyCategoryManager()
    
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    classification = models.ForeignKey(
        'MorphologyClassification',
        on_delete=models.CASCADE,
        related_name='categories',
        blank=True,
        null=True,
    )

    description = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name_en
    
    def natural_key(self):
        return (self.name,)
