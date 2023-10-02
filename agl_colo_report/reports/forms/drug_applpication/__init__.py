from email.policy import default
from django import forms
from reports.models import DrugApplication, Drug, Unit
from django.forms import modelformset_factory


class DrugApplicationForm(forms.ModelForm):
    drug = forms.ModelChoiceField(
        queryset=Drug.objects.all(),
        disabled=True
    )
    value = forms.IntegerField(widget=forms.NumberInput)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all())

    class Meta:
        model = DrugApplication
        fields = [
            # "name",
            "drug",
            "value",
            "unit"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


DrugApplicationFormSet = modelformset_factory(
    DrugApplication, 
    form=DrugApplicationForm, 
    extra=0
)
