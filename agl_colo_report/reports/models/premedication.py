from django.db import models
from .drug import Drug
from .drug_application import DrugApplication

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

    def save(self, *args, **kwargs):
        """
        Override the save method to create associated DrugApplication objects
        """
        # First, call the original save method to save the Premedication instance
        super().save(*args, **kwargs)

        # Fetch some Drug objects (you can customize this query as needed)
        drugs_to_apply = Drug.objects.filter() # TODO: add filter with growing drug database


        # Create a DrugApplication object for each Drug
        for drug in drugs_to_apply:
            DrugApplication.objects.create(
                premedication=self,
                drug=drug,
                value=None,  # You can set default values here
                unit=drug.preferred_unit  # Assume each Drug has a preferred_unit
            )