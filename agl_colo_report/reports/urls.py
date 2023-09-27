from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    # AJAX endpoints
    # path("fetch_patients/", views.fetch_patients, name="fetch_patients"),
    # path('fetch_patient_form/', views.fetch_patient_form, name='fetch_patient_form'),
    # path('fetch_patient_form/<int:patient_id>/', views.fetch_patient_form, name='fetch_patient_form'),
    # # path('fetch_report_form/', views.fetch_report_form, name='fetch_report_form'), ??????
    # path('create_report_form/<int:patient_id>/', views.create_report_form, name='create_report_form'),
    # path('fetch_report_form/<int:report_id>/', views.fetch_report_form, name='fetch_report_form'),
    # path(
    #     "fetch_reports_for_patient/<int:patient_id>/",
    #     views.fetch_reports_for_patient,
    #     name="fetch_reports_for_patient",
    # ),
    # path(
    #     "fetch_report_preview/<int:report_id>/",
    #     views.fetch_report_preview,
    #     name="fetch_report_preview",
    # ),

    # # Standard Django views
    # path('create_patient/', views.PatientCreateView.as_view(), name='create_patient'),
    # path('update_patient/<int:pk>/', views.PatientUpdateView.as_view(), name='update_patient'),
    # path('create_report/', views.ReportCreateView.as_view(), name='create_report'),
    # path('update_report/<int:pk>/', views.ReportUpdateView.as_view(), name='update_report'),


    ### OLD
    # path('add_patient/', views.add_patient, name='add_patient'),
    # path('create_report/', views.create_report, name='create_report'),
    # path('fetch_report/<int:report_id>/', views.fetch_report, name='fetch_report'),
    # path('fetch_report/', views.fetch_report, name='fetch_report_new'),
    # path('fetch_patient/<int:patient_id>/', views.fetch_patient, name='fetch_patient'),
    # path('fetch_patient/', views.fetch_patient, name='fetch_patient_new'),
    # path('get_deepest_insertion_choices/', views.get_deepest_insertion_choices, name='get_deepest_insertion_choices'),
]
