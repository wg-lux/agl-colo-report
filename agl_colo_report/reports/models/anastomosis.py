from django.db import models
from .organ_component import OrganComponent
from .anastomosis_type import AnastomosisType

class Anastomosis(models.Model):
    component_1 = models.ForeignKey(OrganComponent, related_name='component1_anastomoses', on_delete=models.CASCADE)
    connection_type_1 = models.ForeignKey(AnastomosisType, related_name='connection1_anastomoses', on_delete=models.CASCADE)
    component_2 = models.ForeignKey(OrganComponent, related_name='component2_anastomoses', on_delete=models.CASCADE)
    connection_type_2 = models.ForeignKey(AnastomosisType, related_name='connection2_anastomoses', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_de = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else f"{self.component_1.name} to {self.component_2.name}"
