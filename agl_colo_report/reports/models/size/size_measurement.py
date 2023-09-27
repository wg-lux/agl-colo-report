from django.db import models
  
class SizeMeasurement(models.Model):
    value = models.FloatField()
    unit = models.ForeignKey(
        'Unit',
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.value} {self.unit.abbreviation}"
    
    def natural_key(self):
        return (self.name,)

