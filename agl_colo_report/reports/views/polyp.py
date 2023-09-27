from django.http import JsonResponse
from ..models import ColonPolyp

def add_polyp(request, report_id):
    # Your code to add a new polyp associated with the report goes here.
    # Return the new polyp's ID or some other identifier.

    polyp = ColonPolyp.objects.create(report_id=report_id)
    new_polyp_id = polyp.pk

    return JsonResponse({'status': 'success', 'new_polyp_id': new_polyp_id})

def remove_polyp(request, polyp_id):
    # Your code to remove a polyp by its ID goes here.
    ColonPolyp.objects.filter(pk=polyp_id).delete()
    
    return JsonResponse({'status': 'success'})
