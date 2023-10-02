from django.db import models
from .colon_polyp import (
    ColonPolyp,
)

class ReportFindings(models.Model):
    report = models.OneToOneField(
        'Report', on_delete=models.CASCADE, related_name='findings'
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Findings for {self.report.pk}"
    
    def create_polyp(self, polyp_data = None):
        if polyp_data is None:
            polyp_data = {}

        polyp = ColonPolyp.objects.create(
            report_findings=self,
            **polyp_data
        )

        polyp.refresh_from_db()
        return polyp
    

