import re
from django.db import models
    
class ColonPolypMorphology(models.Model):
    polyp = models.OneToOneField(
        'ColonPolyp',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='morphology',
    )
    categorical = models.ForeignKey(
        "MorphologyCategory",
        related_name = 'colon_polyps_categorical',
        on_delete=models.CASCADE,
    )

    paris = models.ForeignKey(
        "MorphologyCategory",
        on_delete=models.CASCADE,
        related_name='colon_polyps_paris',
    )

    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
