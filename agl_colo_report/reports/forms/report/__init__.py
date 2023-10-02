from django import forms
from django.forms import DateInput
from reports.models import Report

class ReportForm(forms.ModelForm):


    class Meta:
        model = Report
        fields = [
            # "id",
            "date_of_procedure",
            "altered_colon_anatomy",
            "colon_anatomy",
            "deepest_insertion",
        ]
        widgets = {
            'date_of_procedure': DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
