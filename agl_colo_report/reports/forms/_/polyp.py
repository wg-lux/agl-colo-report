from django import forms
from ..models import (
    ColonPolyp,
    ColonPolypMorphology,
    ColonPolypLocation,
    Report,
    OrganComponent,
    Anastomosis,
)
from django.forms import inlineformset_factory

class ColonPolypForm(forms.ModelForm):
    class Meta:
        model = ColonPolyp
        fields = ["description"]  # remove location when we add other attributes

ColonPolypFormSet = inlineformset_factory(
    Report,  # parent model
    ColonPolyp,  # inline model
    form=ColonPolypForm,
    extra=0,  # one empty form
    can_delete=True,  # allow deleting
)

class ColonPolypLocationForm(forms.ModelForm):
    class Meta:
        model = ColonPolypLocation
        fields = [
            "organ_component",
            "anastomosis",
            "description",
            "cm",
        ]  # Add fields that are relevant to your model

    organ_component = forms.ModelChoiceField(
        queryset=OrganComponent.objects.all(), required=False
    )

    anastomosis = forms.ModelChoiceField(
        queryset=Anastomosis.objects.all(), required=False
    )


class ColonPolypMorphologyForm(forms.ModelForm):
    class Meta:
        model = ColonPolypMorphology
        fields = [
        ]  # Add fields that are relevant to your model
