from django import forms
from reports.models import (
    ColonPolyp,
    ColonPolypLocation,
    ColonPolypMorphology,
    ColonPolypSize,
    ReportFindings
)
from django.forms import inlineformset_factory, ModelForm

class ColonPolypLocationForm(ModelForm):
    class Meta:
        model = ColonPolypLocation
        fields = ['organ_component', 'description', "cm_from_anal_verge"]

class ColonPolypMorphologyForm(ModelForm):
    class Meta:
        model = ColonPolypMorphology
        fields = ['categorical', 'paris', 'description']

class ColonPolypSizeForm(ModelForm):
    class Meta:
        model = ColonPolypSize
        fields = ['categorical', 'measurement']

class ColonPolypForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ColonPolypForm, self).__init__(*args, **kwargs)
        
        # Initialize nested forms
        self.location_form = ColonPolypLocationForm(
            instance=self.instance.location if self.instance else None,
            prefix=f"{self.prefix}-location",
        )
        self.morphology_form = ColonPolypMorphologyForm(
            instance=self.instance.morphology if self.instance else None,
            prefix=f"{self.prefix}-morphology",
        )
        self.size_form = ColonPolypSizeForm(
            instance=self.instance.size if self.instance else None,
            prefix=f"{self.prefix}-size",
        )

    def save(self, commit=True):
        instance = super(ColonPolypForm, self).save(commit=False)
        
        if commit:
            instance.save()
        
        # Save nested forms
        self.location_form.instance = instance.location
        self.location_form.save(commit=commit)
        
        self.morphology_form.instance = instance.morphology
        self.morphology_form.save(commit=commit)
        
        self.size_form.instance = instance.size
        self.size_form.save(commit=commit)
        
        return instance

    class Meta:
        model = ColonPolyp
        fields = ['report_findings', 'description']

ColonPolypFormSet = inlineformset_factory(
    ReportFindings, ColonPolyp, form=ColonPolypForm, extra=0
)