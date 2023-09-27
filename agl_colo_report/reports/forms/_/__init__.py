from django import forms
from .polyp import (
    ColonPolypForm,
    ColonPolypLocationForm,
    ColonPolypMorphologyForm,
    ColonPolypFormSet,
)
from ...models import (
    Unit,
    Patient,
    Report,
    ColonAnatomy,
    OrganComponent,
    ColonPolyp,
    ColonPolypLocation,
    Anastomosis,
)
from django.forms import inlineformset_factory, DateInput
from datetime import date


# Form to capture patient data
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "dob", "gender"]

    dob = forms.DateField(
        widget=DateInput(attrs={"type": "date"}), initial=date.today()
    )


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "patient",
            "date_of_procedure",
            "altered_colon_anatomy",
            "colon_anatomy",
            "deepest_insertion",
        ]

    date_of_procedure = forms.DateField(
        widget=DateInput(attrs={"type": "date"}), initial=date.today()
    )

    colon_anatomy = forms.ModelChoiceField(
        queryset=ColonAnatomy.objects.all(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the PremedicationFormSet
        self.premedication_formset = PremedicationFormSet(
            instance=self.instance,
            data=self.data if self.is_bound else None,
        )

        # Prepopulate choices for deepest_insertion
        if self.instance.id:
            available_segments = self.instance.get_available_segments()
        else:
            try:
                default_anatomy = ColonAnatomy.objects.get_by_natural_key(
                    "colon-normal"
                )
                available_segments = default_anatomy.available_segments.all()
            except ColonAnatomy.DoesNotExist:
                available_segments = OrganComponent.objects.none()

        # Order the available_segments by component_order_id in descending order
        available_segments = available_segments.order_by("component_order_id")

        # Set the queryset for choices for deepest_insertion
        self.fields["deepest_insertion"].queryset = available_segments

        # Set the default value to the OrganComponent with the highest component_order_id
        default_organ_component = available_segments.first()
        if default_organ_component:
            self.fields["deepest_insertion"].initial = default_organ_component.id

class UnitForm(forms.Form):
    class Meta:
        model = Unit
        # fields = ["name", ...] # omit the fields you don't want to show

    # further specifications for the fields, e.g.: if required or not

from ..models import Premedication


class PremedicationForm(forms.ModelForm):
    class Meta:
        model = Premedication
        fields = [
            "blood_oxygen_monitoring",
            "blood_pressure_monitoring",
            "ecg_monitoring",
        ]

    blood_oxygen_monitoring = forms.BooleanField(initial = True, required=False)
    blood_pressure_monitoring = forms.BooleanField(initial = True, required=False)
    ecg_monitoring = forms.BooleanField(initial = False, required=False)

#TODO use predefined form
PremedicationFormSet = inlineformset_factory(
    Report,
    Premedication,
    form = PremedicationForm,
    fields=('blood_oxygen_monitoring', 'blood_pressure_monitoring', 'ecg_monitoring'),  # Include the fields you want
    extra=1,
    can_delete=False,
)


from ..models import Drug, DrugApplication, Unit
class DrugApplicationForm(forms.ModelForm):
    class Meta:
        model = DrugApplication
        fields = [
            # "drug",
            "value",
            "unit",
        ]

    # drug = forms.ModelChoiceField(queryset=Drug.objects.all())
    try:
        default_unit = Unit.objects.get_by_natural_key('milligram')
    except: 
        # First db creation get_by_natural_key does 
        # not work as the tables are not yet created
        # so this is a workaround which requires us to migrate two times
        # on initial setuo
        default_unit = None
    value = forms.IntegerField(required=False)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), initial=default_unit)

from django.forms import BaseInlineFormSet

DrugApplicationFormSet:BaseInlineFormSet = inlineformset_factory(
    Premedication,
    DrugApplication,
    form=DrugApplicationForm,
    extra=0,
    can_delete=False,
)
