from django.db import models
from django.utils.html import format_html, mark_safe

class ColonPolypLocation(models.Model):
    polyp = models.OneToOneField(
        'ColonPolyp',
        related_name='location',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    organ_component = models.ForeignKey("OrganComponent", related_name='polyp_locations', blank=True, null=True, on_delete=models.CASCADE)
    anastomosis = models.ForeignKey("Anastomosis", related_name='polyp_locations', blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)
    # colon_anatomy = models.ForeignKey(ColonAnatomy, related_name='polyp_locations', blank=True, null=True, on_delete=models.CASCADE)
    cm_from_anal_verge = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.description if self.description else f"No Description for {self.id}"
    
    def get_preview_html(self):
        # Initialize an empty list to collect HTML fragments
        html_fragments = []

        # Add organ component if available
        if self.organ_component:
            html_fragments.append(format_html('<h4>Organ Component:</h4> <p>{}</p>', self.organ_component))

        # Add anastomosis if available
        if self.anastomosis:
            html_fragments.append(format_html('<h4>Anastomosis:</h4> <p>{}</p>', self.anastomosis))

        # Add description if available
        if self.description:
            html_fragments.append(format_html('<h4>Description:</h4> <p>{}</p>', self.description))

        # Add colon anatomy if available
        if self.colon_anatomy:
            html_fragments.append(format_html('<h4>Colon Anatomy:</h4> <p>{}</p>', self.colon_anatomy))

        # Add cm if available
        if self.cm is not None:  # Checking for None because 0 is a valid integer
            html_fragments.append(format_html('<h4>CM:</h4> <p>{}</p>', self.cm))

        # Combine all fragments into a single HTML string
        return mark_safe(''.join(html_fragments))

    
