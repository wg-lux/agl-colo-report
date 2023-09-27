from django.shortcuts import render
from ..models import Patient

# View for the landing page
def landing_page(request):
    patients = Patient.objects.prefetch_related('reports').all()  # Fetch all existing patients along with their reports
    return render(request, 'landing_page.html', {'patients': patients})
