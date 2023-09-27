from ..models import Premedication, ColonPolyp, Drug, Report
from ..forms import (
    DrugApplicationFormSet,
    PremedicationFormSet,
    ColonPolypFormSet,
)

from django.shortcuts import get_object_or_404


def get_premedication_formset(report_id=None, premedication_id=None):
    if premedication_id:
        premedication = get_object_or_404(Premedication, id=premedication_id)
        report = premedication.report
    elif report_id:
        print()
        report = get_object_or_404(Report, id=report_id)
        premedication = report.premedication
    else:
        raise ValueError("Either premedication_id or report_id must be provided")

    premedication_formset = PremedicationFormSet(
        instance=report, prefix="premedication"
    )
    # get length of premedication_formset
    len_premedication_formset = len(premedication_formset)
    assert (
        len_premedication_formset == 1
    ), "PremedicationFormSet should have only one form"
    premedication_formset.management_form.fields[
        "INITIAL_FORMS"
    ].initial = len_premedication_formset
    premedication_formset.management_form.fields[
        "TOTAL_FORMS"
    ].initial = len_premedication_formset

    return premedication_formset


def get_drug_application_formset(report_id=None, premedication_id=None):
    if premedication_id:
        premedication = get_object_or_404(Premedication, id=premedication_id)
        report = premedication.report
    elif report_id:
        report = get_object_or_404(Report, id=report_id)
        premedication = report.premedication
    else:
        raise ValueError("Either premedication_id or report_id must be provided")

    drug_application_formset = DrugApplicationFormSet(
        instance=premedication, prefix="drugapp"
    )
    # prefetch drug objects of each drug application
    drugs = [
        drug_application.instance.drug for drug_application in drug_application_formset
    ]
    drug_application_formset.management_form.fields["INITIAL_FORMS"].initial = len(
        drugs
    )
    drug_application_formset.management_form.fields["TOTAL_FORMS"].initial = len(drugs)

    return drugs, drug_application_formset


def get_polyp_formset(report_id=None):
    if report_id:
        report = get_object_or_404(Report, id=report_id)
    else:
        raise ValueError("report_id must be provided")

    # get queryset of polyps
    polyps = ColonPolyp.objects.filter(report=report)
    # check if queryset is empty
    if polyps:
        polyp_formset = ColonPolypFormSet(instance=report, prefix="polyp")
    else:
        polyp_formset = ColonPolypFormSet(instance=report, initial=[], prefix="polyp")

    polyp_formset.management_form.fields["INITIAL_FORMS"].initial = len(polyps)
    polyp_formset.management_form.fields["TOTAL_FORMS"].initial = len(polyps)

    polyp_attribute_forms = []
    for polyp in polyps:
        polyp_attribute_forms.append(get_polyp_attribute_forms(polyp_id=polyp.id))

    return polyp_formset, polyp_attribute_forms


from ..forms import ColonPolypLocationForm, ColonPolypMorphologyForm

def get_polyp_attribute_forms(polyp_id=None):
    if polyp_id:
        polyp = get_object_or_404(ColonPolyp, id=polyp_id)
    else:
        raise ValueError("Either polyp_id must be provided")

    forms = {
        f"polyp_location": ColonPolypLocationForm(
            instance=polyp, prefix=f"polyp_location_{polyp_id}"
        ),
        f"polyp_morphology": ColonPolypMorphologyForm(
            instance=polyp, prefix=f"polyp_morphology_{polyp_id}"
        ),
    }

    return forms
