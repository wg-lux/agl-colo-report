from django.db import models
from .patient import Patient
from .colon_anatomy import ColonAnatomy
from .organ_component import OrganComponent
from .premedication import Premedication
from django.utils.html import format_html, mark_safe
from django.utils.timezone import now

ALTERED_COLON_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
        ("unknown", "Unknown"),
    ]

def get_altered_colon_choices_default():
    return ALTERED_COLON_CHOICES[2][0]

import warnings

class Report(models.Model):
    patient = models.ForeignKey(
        Patient, related_name="reports", on_delete=models.CASCADE
    )

    date_of_procedure = models.DateField(default=now)

    altered_colon_anatomy = models.CharField(
        max_length=10, choices=ALTERED_COLON_CHOICES, default="no"
    )

    try:
        colon_anatomy = models.ForeignKey(
            ColonAnatomy,
            default=ColonAnatomy.objects.get_by_natural_key("colon-normal").id,
            null=True,
            on_delete=models.SET_NULL,
        )
    except:
        colon_anatomy = models.ForeignKey(
            ColonAnatomy, null=True, on_delete=models.SET_NULL
        )

    deepest_insertion = models.ForeignKey(
        OrganComponent, null=True, blank=True, on_delete=models.SET_NULL
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to automatically create an associated
        Premedication object whenever a new Report object is created.
        """
        # Use this flag to identify if the object is new
        is_new = self.pk is None

        # if a new report is created, we need to assign some default values and create some objects
        if is_new:
            # get colon anatomy "unknown" and set it
            try:
                colon_anatomy = ColonAnatomy.objects.get_by_natural_key("colon-unknown")
                self.colon_anatomy = colon_anatomy
                self.deepest_insertion = self.get_available_segments_ordered().first()
                self.altered_colon_anatomy = get_altered_colon_choices_default()
                
            except ColonAnatomy.DoesNotExist:
                warnings.warn("Colon anatomy 'colon-unknown' does not exist. Please create it in the admin interface.")
                assert False

        # First, call the original save method to save the Report instance
        super().save(*args, **kwargs)

        # If it's a new Report object, create a corresponding Premedication object
        if is_new:
            Premedication.objects.create(report=self)


    # The class ColonPolyp has a foreign key to Report with the related name 'polyps'

    def get_available_segments_ordered(self):
        return self.colon_anatomy.get_available_segments_ordered()

    def get_preview_html(self):
        # Initialize an empty list to collect HTML fragments
        html_fragments = []

        # Add patient information
        html_fragments.append(
            format_html("<h4>Patient:</h4> <p>ID: {}</p>", self.patient.id)
        )

        # Add date of procedure
        html_fragments.append(
            format_html("<h4>Date of Procedure:</h4> <p>{}</p>", self.date_of_procedure)
        )

        # Add altered colon anatomy status
        html_fragments.append(
            format_html(
                "<h4>Altered Colon Anatomy:</h4> <p>{}</p>",
                self.get_altered_colon_anatomy_display(),
            )
        )

        # Add colon anatomy if available
        if self.colon_anatomy:
            html_fragments.append(
                format_html("<h4>Colon Anatomy:</h4> <p>{}</p>", self.colon_anatomy)
            )

        # Add deepest insertion if available
        if self.deepest_insertion:
            html_fragments.append(
                format_html(
                    "<h4>Deepest Insertion:</h4> <p>{}</p>", self.deepest_insertion
                )
            )

        # Add associated polyps
        polyps = (
            self.polyps.all()
        )  # Assuming the related_name for the ForeignKey in ColonPolyp to Report is 'polyps'
        if polyps.exists():
            html_fragments.append("<h4>Polyps:</h4>")
            for polyp in polyps:
                html_fragments.append("<hr>")
                html_fragments.append(polyp.get_preview_html())
                html_fragments.append("<hr>")

        # Combine all fragments into a single HTML string
        return mark_safe("".join(html_fragments))
