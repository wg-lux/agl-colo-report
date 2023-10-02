# models/drug_application.py

from django.db import models
from .drug import Drug
from .shared.unit import Unit


class DrugApplication(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    premedication = models.ForeignKey(
        "Premedication", on_delete=models.CASCADE, related_name="drug_applications"
    )
    drug = models.ForeignKey(
        Drug,
        on_delete=models.CASCADE,
    )
    value = models.IntegerField(default=0, null=True, blank=True)
    unit = models.ForeignKey(
        Unit,
        null=True,  # shouldnt happen, only for cascading where we want to set null
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        str_repr = f"{self.drug} {self.value} {self.drug.preferred_unit.abbreviation}"
        return str_repr

    # TODO
