# views/api/polyp_views.py

from django.http import JsonResponse
from reports.serializers import ColonPolypSerializer



# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ...models import ColonPolyp
from reports.serializers import ColonPolypSerializer

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
