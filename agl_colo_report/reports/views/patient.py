from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from ..forms import PatientForm
from ..models import Patient
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

def fetch_patients(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'  # Check if it's an AJAX request
    if is_ajax:  # Check if it's an AJAX request
        patients = serialize('json', Patient.objects.all())
        return JsonResponse({'patients': patients}, safe=False)
    else:
        patients = Patient.objects.all()
        return render(request, 'fetch_patients.html', {'patients': patients})

def fetch_patient(request, patient_id=None):
    if patient_id:
        patient = get_object_or_404(Patient, id=patient_id)
        form = PatientForm(instance=patient)
    else:
        form = PatientForm()

    html_content = render_to_string('patient_form_partial.html', {'patient_form': form}, request)
    return HttpResponse(html_content)

# Fetch patient form for editing
def fetch_patient_form(request, patient_id=None):
    if patient_id:
        patient = get_object_or_404(Patient, id=patient_id)
        form = PatientForm(instance=patient)
    else:
        form = PatientForm()

    html_content = render_to_string('patient_form_partial.html', {'patient_form': form}, request)
    return HttpResponse(html_content)


@csrf_exempt
def save_patient(request, patient_id=None):
    if request.method == 'POST':
        # Update existing patient if patient_id is provided; otherwise, create new
        instance = Patient.objects.get(id=patient_id) if patient_id else None
        form = PatientForm(request.POST, instance=instance)
        if form.is_valid():
            patient = form.save()
            return JsonResponse({'status': 'success', 'patient_id': patient.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

# Create and Update views for Patient
# class PatientCreateView(CreateView):
#     model = Patient
#     form_class = PatientForm
#     template_name = 'patient_form.html'
#     success_url = reverse_lazy('landing_page')

# class PatientUpdateView(UpdateView):
#     model = Patient
#     form_class = PatientForm
#     template_name = 'patient_form.html'
#     success_url = reverse_lazy('landing_page')