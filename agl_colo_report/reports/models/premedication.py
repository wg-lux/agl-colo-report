from django.db import models
from .drug import Drug
from .drug_application import DrugApplication

PREMEDICATION_DRUG_NATURAL_KEYS = [
    "propofol",
    "midazolam",
    "oxygen"
]

class Premedication(models.Model):
    report = models.OneToOneField(
        'Report', on_delete=models.CASCADE,
        primary_key=True,
        related_name = "premedication"
        )
    blood_oxygen_monitoring = models.BooleanField(default=True)
    blood_pressure_monitoring = models.BooleanField(default=True)
    ecg_monitoring = models.BooleanField(default=False)
    # model is ForeignKey to DrugApplication, there we defined the related_name "drug_applications"

    def create_drug_applications(self):
        # Fetch drugs by natural keys (PREMEDICATION_DRUG_NATURAL_KEYS)
        drugs_to_apply = Drug.objects.filter(
            name__in=PREMEDICATION_DRUG_NATURAL_KEYS
        )

        # Create a DrugApplication object for each Drug
        for drug in drugs_to_apply:
            DrugApplication.objects.create(
                premedication=self,
                drug=drug,
                unit=drug.preferred_unit  # Assume each Drug has a preferred_unit
            )

    def save(self, *args, **kwargs):
        """
        Override the save method to create associated DrugApplication objects
        """
        # First, call the original save method to save the Premedication instance
        super().save(*args, **kwargs)
            