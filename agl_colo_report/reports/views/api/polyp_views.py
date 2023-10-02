# views/api/polyp_views.py

from django.http import JsonResponse
from reports.serializers import ColonPolypSerializer



# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ...models import ColonPolyp
from reports.serializers import ColonPolypSerializer
from django.shortcuts import get_object_or_404
from reports.models import ReportFindings, Report

class CreateColonPolypAPIView(APIView):

    def post(self, request, format=None):
        report_id = request.data.get('report_id', None)
        if report_id is None:
            return Response({"error": "report_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # get report by id
        report = get_object_or_404(Report, id=report_id)
        report_findings:ReportFindings = report.findings
        
        _polyp = report_findings.create_polyp()
        
        return Response({"message": "Polyp created successfully"}, status=status.HTTP_201_CREATED)





################# OLD API VIEWS #####################
class ColonPolypListCreateView(generics.ListCreateAPIView):
    queryset = ColonPolyp.objects.all()
    serializer_class = ColonPolypSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Additional logic for saving the object can go here
        serializer.save()

class ColonPolypRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ColonPolyp.objects.all()
    serializer_class = ColonPolypSerializer

    def perform_update(self, serializer):
        # Additional logic for updating the object can go here
        serializer.save()

    def perform_destroy(self, instance):
        # Additional logic for deleting the object can go here
        instance.delete()
