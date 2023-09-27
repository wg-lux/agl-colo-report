# django ajax api for patient

from django.http import JsonResponse
from ...models import Patient
from reports.serializers import PatientSerializer

def get_patient(request):
    patient_id = request.GET.get("patient_id")
    patient = Patient.objects.get(id=patient_id)
    patient_serialized = PatientSerializer(patient).data

    return JsonResponse(patient_serialized, safe=False)


def get_patients(request):
    patients = Patient.objects.all()
    patients_serialized = PatientSerializer(patients, many=True).data

    return JsonResponse(patients_serialized, safe=False)



