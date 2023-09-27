from django.db import models
from ..size import SizeCategory, SizeClassification

class ColonPolypSize(models.Model):
    polyp = models.OneToOneField(
        'ColonPolyp',
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='size',
    )

    # Options are all SizeCategory objects that have a size_classification == "polyp-size-categories-regular"
    categorical = models.ForeignKey(
        SizeCategory,
        on_delete=models.CASCADE,
        related_name='colon_polyps_categorical',
        null=True,
        blank=True,
    )

    measurement = models.OneToOneField(
        'SizeMeasurement',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='colon_polyp_size',
    )

    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def get_size_classifications(self):
        return SizeClassification.objects.filter(
            pathology_types__in=self.polyp.pathology_types.all()
        ).distinct()
    
    def get_size_categorical_choices(self):
        return SizeCategory.objects.filter(
            size_classification__in=["polyp-size-categories-regular"]
        ).distinct()