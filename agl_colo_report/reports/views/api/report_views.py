
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from reports.models import (
    Report,
    Patient,
    ColonAnatomy,
    OrganComponent,
)
from reports.serializers import ReportSerializer
from django.shortcuts import get_object_or_404
from reports.forms import ReportForm
from django.http import JsonResponse

class ReportListTableView(generics.ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        patient_id = self.request.query_params.get('patient_id', None)
        if patient_id is not None:
            queryset = Report.objects.filter(patient_id=patient_id)
            # Return the queryset, which could be empty but not a 404 error
            return queryset
        return Report.objects.none()  # Return an empty queryset

def get_default_report_data():
    default_anatomy = ColonAnatomy.objects.get_by_natural_key('colon-normal')
    default_deepest_insertion = OrganComponent.objects.get_by_natural_key('cecum')
    default_report_data = {
        "altered_colon_anatomy": "no",
        "colon_anatomy": default_anatomy,
        "deepest_insertion": default_deepest_insertion,
    }
    return default_report_data

class CreateReportAPIView(APIView):

    def post(self, request, format=None):
        patient_data = request.data.get('patient', None)
        # patient_data = request.data # currently we only post patient data
        if patient_data is None:
            return Response({"error": "Patient data is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        patient = get_object_or_404(Patient, id=patient_data['id'])
        # create empty report for Patient
        _default_report_data = get_default_report_data()
        print("creating report for patient:")
        print(patient)

        # create empty report for patient using _default_report_data
        report_data = {
            "patient": patient,
            **_default_report_data
        }
        report = Report.objects.create(**report_data)
        serializer = ReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

from reports.forms import (
    PremedicationForm,
    DrugApplicationFormSet,
    ColonPolypFormSet
)

from reports.models import DrugApplication

class GetReportAPIView(APIView):
    def get(self, request, report_id):
        response_data = {}

        if report_id is not None:
            # report form
            report = get_object_or_404(Report, id=report_id)
            report_form = ReportForm(instance=report)
            base_form_data = report_form.as_p()
            response_data['base_form_data'] = base_form_data

            # premedication form
            premedication_form = PremedicationForm(instance=report.premedication)
            premedication_form_data = premedication_form.as_p()
            response_data['premedication_form_data'] = premedication_form_data

            # drug application formset
            existing_drug_applications = DrugApplication.objects.filter(premedication=report.premedication)
            drug_application_formset = DrugApplicationFormSet(queryset=existing_drug_applications)
            drug_application_formset_data = ''.join([str(form) for form in drug_application_formset])
            drug_application_formset_data = f"<p>{drug_application_formset_data}</p><p>{drug_application_formset.management_form}</p>"
            # drug_application_formset_data = f"<p>{drug_application_formset_data}</p>"
            response_data['drug_application_formset_data'] = drug_application_formset_data

            # polyp formset
            report_findings = report.findings
            print("report_findings: ", report_findings)
            polyp_formset = ColonPolypFormSet(instance=report_findings)

            # Initialize an empty list to hold the HTML strings for each form
            polyp_formset_data_list = []

            # Loop through each form in the formset
            ###########################MAKE FUNCTION############################
            for form in polyp_formset:
                # Get the HTML strings for the form and its nested forms
                form_html = str(form)
                location_form_html = str(form.location_form)
                morphology_form_html = str(form.morphology_form)
                size_form_html = str(form.size_form)
                
                # Combine the HTML strings into one string for this form
                combined_form_html = f"<div class='polyp-form'>\
                                        <h3>Polyp Form</h3>\
                                        {form_html}\
                                        <h4>Location</h4>\
                                        {location_form_html}\
                                        <h4>Morphology</h4>\
                                        {morphology_form_html}\
                                        <h4>Size</h4>\
                                        {size_form_html}\
                                    </div>"
                
                # Add the combined HTML string to the list
                polyp_formset_data_list.append(combined_form_html)

            # Join all the form HTML strings into one string for the entire formset
            polyp_formset_data = ''.join(polyp_formset_data_list)

            # Add the management form
            polyp_formset_data = f"<div class='polyp-formset'>\
                                    {polyp_formset_data}\
                                    <div class='management-form'>\
                                    {polyp_formset.management_form}\
                                    </div>\
                                </div>"

            # Pretty print polyp_formset_data
            print("polyp_formset_data: ", polyp_formset_data)
            ################################MAKE FUNCTION###########################
            response_data["polyp_formset_data"] = polyp_formset_data

            return Response(response_data)          

import json
from django.http import QueryDict

class UpdateReportAPIView(APIView):
    def put(self, request, report_id):
        report = get_object_or_404(Report, id=report_id)

        report_form_data = json.loads(request.data.get('base_form_data', '{}'))
        if isinstance(report_form_data, str):
            report_form_data = QueryDict(report_form_data)
        report_form = ReportForm(report_form_data, instance=report)

        premedication_form_data = json.loads(request.data.get('premedication_form_data', '{}'))
        if isinstance(premedication_form_data, str):
            premedication_form_data = QueryDict(premedication_form_data)
        premedication_form = PremedicationForm(premedication_form_data, instance=report.premedication)

        drug_application_formset_data = json.loads(
            request.data.get(
                'drug_application_formset_data',
                '{}'
            ))
        if isinstance(drug_application_formset_data, str):
            drug_application_formset_data = QueryDict(drug_application_formset_data)
        
        existing_drug_applications = DrugApplication.objects.filter(premedication=report.premedication)
        drug_application_formset = DrugApplicationFormSet(
            drug_application_formset_data,
            queryset=existing_drug_applications
        )

        if report_form.is_valid() and premedication_form.is_valid():
            # Save these forms first as they are valid
            report_form.save()
            premedication_form.save()

            # Now check the drug application formset
            if drug_application_formset.is_valid():
                drug_application_formset.save()
                return Response({"message": "Report updated successfully"}, status=status.HTTP_200_OK)
            else:
                print("drug_application_formset errors: ", drug_application_formset.errors)
                return Response({"message": "Invalid drug application data"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print("report_form errors: ", report_form.errors)
            print("premedication_form errors: ", premedication_form.errors)
            return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)



############### OLD / admin API #####################
class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Additional logic for saving the object can go here
        serializer.save()

class ReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_update(self, serializer):
        # Additional logic for updating the object can go here
        serializer.save()

    def perform_destroy(self, instance):
        # Additional logic for deleting the object can go here
        instance.delete()

