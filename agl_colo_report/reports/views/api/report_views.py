
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ...models import Report  
from reports.serializers import ReportSerializer 

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

