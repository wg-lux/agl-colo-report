from django import forms
from django.forms import DateInput
from reports.models import Premedication

class PremedicationForm(forms.ModelForm):
    class Meta:
        model = Premedication
        fields = [
            "blood_oxygen_monitoring",
            "blood_pressure_monitoring",
            "ecg_monitoring",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def as_p(self):
        custom_html = []

        checkbox_html = '<div class="checkbox-row">'
        for field in self:
            if field.field.widget.input_type == 'checkbox':
                checkbox_html += f'<label>{field.label}: {field}</label>'
        checkbox_html += '</div>'
        
        custom_html.append(checkbox_html)
        
        return ''.join(custom_html)

