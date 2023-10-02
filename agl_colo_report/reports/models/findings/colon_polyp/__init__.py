from django.db import models
from ...pathology_type import PathologyType
from .colon_polyp_location import ColonPolypLocation
from .colon_polyp_morphology import ColonPolypMorphology
from .colon_polyp_size import ColonPolypSize

from django.utils.html import format_html, mark_safe

# class ColonPolypPersistence(models.Model):
#     patient = models.ForeignKey(Patient, related_name='polyp_persistences', on_delete=models.CASCADE)


class ColonPolyp(models.Model):
    report_findings = models.ForeignKey("ReportFindings", related_name="polyps", on_delete=models.CASCADE)
    pathology_types = models.ManyToManyField(PathologyType, related_name="colon_polyps")
    description = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(
            *args, **kwargs
        )  # Call the original save method first to get an id
        if not self.pathology_types.exists():  # Check if pathology_types is empty
            pathology_types = PathologyType.objects.get_by_natural_keys(
                "colon-pathology", "polyp"
            )
            self.pathology_types.set(pathology_types)

        if is_new:
            ColonPolypLocation.objects.create(polyp=self)
            ColonPolypMorphology.objects.create(polyp=self)
            ColonPolypSize.objects.create(polyp=self)

    def get_preview_html(self):
        # Initialize an empty list to collect HTML fragments
        html_fragments = []

        # Add organ component if available
        if self.location:
            location_html = self.location.get_preview_html()
            html_fragments.append(format_html("<h4>Location:</h4> {}", location_html))

        # Combine all fragments into a single HTML string
        return mark_safe("".join(html_fragments))
