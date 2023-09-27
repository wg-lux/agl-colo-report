from django.http import JsonResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from reports.models import Patient
from reports.serializers import PatientSerializer
from reports.forms import PatientForm

class PatientAPIView(APIView):
    def get(self, request):
        # Create a form instance with any initial data you need.
        form = PatientForm()
        form_html = form.as_p()  # You can choose other rendering methods like as_table(), as_ul(), etc.

        return JsonResponse({'patient_form_html': form_html})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})


class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientUpdateView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
