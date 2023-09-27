from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import ColonAnatomy, OrganComponent

def get_available_segments(request, colon_anatomy_id):
    try:
        anatomy = ColonAnatomy.objects.get(id=colon_anatomy_id)
        available_segments = anatomy.available_segments.all().values('id', 'name')
        return JsonResponse(list(available_segments), safe=False)
    except ColonAnatomy.DoesNotExist:
        return JsonResponse([], safe=False)

# def save_formset(formset, instance, name):
#     """
#     Save a formset and link it to an instance using the given name.

#     :param formset: The formset to save
#     :param instance: The parent instance that the formset will be linked to
#     :param name: The name of the related field on the parent model
#     """
#     for form in formset:
#         if form.is_valid():
#             child_instance = form.save(commit=False)
#             setattr(child_instance, name, instance)
#             child_instance.save()

# def get_deepest_insertion_choices(request):
#     altered_colon_anatomy = request.GET.get('altered_colon_anatomy')
#     colon_anatomy_id = request.GET.get('colon_anatomy')
    
#     # Initialize an empty list to hold choices
#     choices_list = []

#     if colon_anatomy_id:
#         colon_anatomy = get_object_or_404(ColonAnatomy, id=colon_anatomy_id)
#         choices = colon_anatomy.available_segments.all().order_by('component_order_id')
#     else:
#         try:
#             default_anatomy = ColonAnatomy.objects.get_by_natural_key('colon-normal')
#             choices = default_anatomy.available_segments.all().order_by('component_order_id')
#         except ColonAnatomy.DoesNotExist:
#             choices = OrganComponent.objects.none()  # Return an empty queryset

#     # Convert QuerySet to a list of dictionaries for JSON serialization
#     for choice in choices:
#         choices_list.append({'value': choice.id, 'label': choice.name})

#     return JsonResponse({'choices': choices_list})