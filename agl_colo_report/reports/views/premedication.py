# from ..models import Premedication, DrugApplication, Drug, Report
# from ..forms import (
#     DrugApplicationFormSet,
#     PremedicationFormSet,
#     ReportForm,
#     DrugApplicationForm
# )

# from django.shortcuts import get_object_or_404



# #### TO DEPRECEATE
# def get_premedication_formset(request=None, premedication_id = None, report_id = None, patient_id = None):
#     # get patient_id from request
    
#     if premedication_id:
#         premedication = get_object_or_404(Premedication, id=premedication_id)
        
#     elif report_id:
#         # if report id, check if a premedication exists for this report
#         # if not, create one
#         report = Report.objects.get(id=report_id)

#         # premedication has foreign_key report
#         # check if a premedication exists for this report
#         if hasattr(report, 'premedication'):
#             premedication = report.premedication
#         else:
#             premedication = Premedication.objects.create(report=report)
        
#     elif request:
#         report = Report.objects.create(patient_id=patient_id)
#         # request is a post request containing the 
#         premedication = Premedication.objects.create(report=report)
#         premedication.save()

#     else:
#         raise ValueError("Either request or premedication_id or report_id must be provided")

#     # Fetch all available drugs
#     all_drugs = Drug.objects.all()

#     # reset logs
#     with open('log.txt', 'w') as f:
#         f.write("")

#     # Ensure a DrugApplication exists for each drug
#     drug_applications = []
#     for drug in all_drugs:
#         drug_application, created = DrugApplication.objects.get_or_create(
#             premedication=premedication,
#             drug=drug,
#         )
#         drug_applications.append(drug_application)

#     # queryset
#     queryset = DrugApplication.objects.filter(premedication=premedication)
#     # Create the DrugApplicationFormSet which contains all DrugApplicationForms
#     drug_application_formset = DrugApplicationFormSet(
#         initial= queryset,
#         instance=premedication,
#             )


#     all_drugs_and_drug_application_forms = list(zip(all_drugs, drug_application_formset))

#     # Refresh the premedication instance and create the premedication_formset
#     premedication.refresh_from_db()
#     premedication_formset = PremedicationFormSet(instance=premedication)
    

#     return report_id, premedication_formset, all_drugs_and_drug_application_forms