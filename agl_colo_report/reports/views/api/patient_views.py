from django.http import JsonResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from reports.models import Patient
from reports.serializers import PatientSerializer
from reports.forms import PatientForm
from django.forms.models import model_to_dict
from .utils import as_bootstrap

class PatientAPIView(APIView):
    def get(self, request):
        # Create a form instance with any initial data you need.
        form = PatientForm()
        form_html = form.as_p() 

        # Convert form to a dictionary representation
        initial_data = model_to_dict(form.instance)

        # Send both HTML and initial data as JSON
        return JsonResponse({'form_html': form_html, 'initial_data': initial_data})


    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

class PatientListTableView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

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
