# import pprint
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, JsonResponse

# from ..forms import (
#     ReportForm,
#     ReportForm,
#     ColonPolypFormSet,
#     ColonPolypForm,
#     ColonPolypLocationForm,
#     DrugApplicationFormSet,
#     ColonPolypMorphologyForm,
# )
# from ..models import Report, Drug
# from django.template.loader import render_to_string  # Import transaction
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, UpdateView
# from django.core.serializers import serialize





# from .formset_helper import (
#     get_premedication_formset,
#     get_drug_application_formset,
#     get_polyp_formset,
# )


# def report_form_helper(report_id):
#     """
#     Fetches the report form and returns the HTML content.
#     """
#     if report_id:
#         report = get_object_or_404(Report, id=report_id)
#         report_form = ReportForm(instance=report)
#     else:
#         raise ValueError("report_id must be provided")

#     # Initialize the formset to show all ColonPolyp objects related to this report
#     polyp_formset, polyp_attribute_forms = get_polyp_formset(report_id=report_id)
#     # Polyp Attribute Forms is a list of dictionaries containing the polyp attribute forms for each polyp
#     premedication_formset = get_premedication_formset(report_id=report_id)
#     drug_list, drugapp_formset = get_drug_application_formset(report_id=report_id)
#     polyps_with_attributes =  zip(polyp_formset, polyp_attribute_forms)
    
#     empty_polyp_form = ColonPolypForm(
#         prefix="polyp_empty",
#         instance = report
#     )
#     empty_polyp_attribute_forms = {
#         "polyp_location": ColonPolypLocationForm(prefix="polyp_location_empty"),
#         "polyp_morphology": ColonPolypMorphologyForm(prefix="polyp_morphology_empty")
#     }
    

#     content = {
#         "report_form": report_form,
#         # "polyp_formset": polyp_formset,
#         "polyps_with_attributs": polyps_with_attributes,
#         "n_initial_polyp_forms": len(polyp_formset.forms),
#         "premedication_formset": premedication_formset,
#         "n_initial_premedication_forms": len(premedication_formset.forms),
#         "drugapp_formset": drugapp_formset,
#         "drug_list": drug_list,
#         "empty_polyp_form": empty_polyp_form,
#         "empty_polyp_attribute_forms": empty_polyp_attribute_forms,
#     }

#     for polyp_attribute_form in polyp_attribute_forms:
#         content.update(polyp_attribute_form)

#     print(content)

#     return content


# def fetch_reports_for_patient(request, patient_id):
#     # get all reports for the patient id
#     reports = Report.objects.filter(patient_id=patient_id).all()
#     reports = serialize("json", reports)
#     return JsonResponse({"reports": reports})  # , safe = False)


# def fetch_report_preview(request, report_id):
#     try:
#         report = Report.objects.get(pk=report_id)
#         preview_html = report.get_preview_html()
#         return HttpResponse(preview_html)
    
#     except Report.DoesNotExist:
#         return JsonResponse(
#             {"status": "error", "error": "Report does not exist"}, status=404
#         )


# # Fetch report form for editing
# def fetch_report_form(request, report_id):
#     content = report_form_helper(report_id=report_id)
#     # html_content = render_to_string("report_form_partial.html", content)

#     return render(request, "report_form_partial.html", content)


# # Fetch report form for creation
# def create_report_form(request, patient_id):
#     report = Report.objects.create(patient_id=patient_id)
#     return JsonResponse({"status": "success", "report_id": report.pk})


# def save_polyp_formset(polyp_formset, report_id):
#     for i, polyp_form in enumerate(polyp_formset.forms):
#         polyp = polyp_form.save(commit=False)
#         polyp.report_id = report_id
#         polyp.save()


# from ..forms import DrugApplicationFormSet, PremedicationFormSet

# # Django view to save the report
# # @csrf_exempt

# import json


# def print_form_data_to_json(request):
#     if request.method == "POST":
#         # Extract POST data from the request
#         post_data = request.POST

#         # Convert the QueryDict to a dictionary
#         data_dict = post_data.dict()

#         # Write to a JSON file
#         with open("form_data.json", "w") as json_file:
#             json.dump(data_dict, json_file, indent=4)

#         return JsonResponse(
#             {"status": "success", "message": "Data written to form_data.json"}
#         )

#     else:
#         return JsonResponse(
#             {"status": "failure", "message": "This function only accepts POST requests"}
#         )


# def save_report(request, report_id=None):
#     if request.method == "POST":
#         report_form = ReportForm(request.POST)
#         print_form_data_to_json(request)
#         if not report_form.is_valid():
#             print("Report form")
#             print(report_form)
#             errors = report_form.errors
#             return JsonResponse({"status": "error", "error": errors}, status=400)
#         assert report_form.is_valid()

#         report_instance = report_form.save(commit=False)
#         report_instance.id = report_id
#         report_instance.save()

    
#         premedication_formset = PremedicationFormSet(
#             request.POST,
#             instance=report_instance,
#             prefix = "premedication"
#             # prefix = "premedication"
#         )
#         assert premedication_formset.is_valid()
#         if not premedication_formset.is_valid():
#             print("Premedication formset")
#             print(premedication_formset)
#             errors = premedication_formset.errors
#             return JsonResponse({"status": "error", "error": errors}, status=400)
#         premedication_formset.save()

#         drug_application_formset = DrugApplicationFormSet(
#             request.POST,
#             instance=premedication_formset.forms[0].instance,
#             prefix = "drugapp"
#         )
#         _valid = drug_application_formset.is_valid()
#         if not _valid:
#             print("Drug application formset")
#             print(drug_application_formset)
#             errors = drug_application_formset.errors
#             return JsonResponse({"status": "error", "error": errors}, status=400)
#         drug_application_formset.save()


#         polyp_formset = ColonPolypFormSet(
#             request.POST,
#             instance=report_instance,
#             prefix="polyp"
#         )
#         if not polyp_formset.is_valid():
#             print("Polyp formset")
#             print(polyp_formset)
#             errors = polyp_formset.errors
#             return JsonResponse({"status": "error", "error": errors}, status=400)

#         assert polyp_formset.is_valid()
#         polyp_formset.save()

#         print("GEWONNEN")

#         return JsonResponse({"status": "success"})

#     else:
#         return JsonResponse(
#             {"status": "error", "error": "Method not allowed"}, status=405
#         )
