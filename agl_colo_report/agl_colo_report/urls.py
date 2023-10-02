"""
URL configuration for agl_colo_report project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from reports import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', include('reports.urls')),
    path('', RedirectView.as_view(url='reports/')),
    path("", views.main, name="main"),

    ## API
    path("api/get_patients", views.api.get_patients, name="get_patients"),
    
    # API VIEWS
    path('api/patient/', views.api.PatientAPIView.as_view(), name='api_patient'),
    # for easier readability and maintainability we use the same view in different urls
    path("api/patient/save/", views.api.PatientAPIView.as_view(), name="save_patient"),
    path('api/patients/', views.api.PatientList.as_view(), name='patient-list'),
    path("api/patients/get-table/", views.api.PatientListTableView.as_view(), name="get_patient_table"),
    path('api/patients/create-view', views.api.PatientCreateView.as_view(), name='get_patient'),
    
    path("api/reports/get-table/", views.api.ReportListTableView.as_view(), name="get_report_table"),    
    path('api/reports/create/', views.api.CreateReportAPIView.as_view(), name='create_report'),
    path('api/reports/get-report/<int:report_id>/', views.api.GetReportAPIView.as_view(), name='get_report'),
    path('api/reports/update-report/<int:report_id>/', views.api.UpdateReportAPIView.as_view(), name='update_report'),
    path("api/reports/list-create-view", views.api.ReportListCreateView.as_view(), name="get_report_list"),
    # path("api/reports/modify-view/<int:pk>/", views.api.ReportRetrieveUpdateDestroyView.as_view(), name="get_report"),
    path("api/colon-polyp/create/", views.api.CreateColonPolypAPIView.as_view(), name="create_colonpolyp"),
    
    
    
    path('api/colonpolyps/create-view', views.api.ColonPolypListCreateView.as_view(), name='colonpolyp-list-create'),
    path('api/colonpolyps/modify/-view/<int:pk>/', views.api.ColonPolypRetrieveUpdateDestroyView.as_view(), name='colonpolyp-retrieve-update-destroy'),
    
    # # AJAX endpoints
    # path("fetch_patients/", views.fetch_patients, name="fetch_patients"),
    # # differentiate create, fetch and update in future? 
    # path('fetch_patient_form/', views.fetch_patient_form, name='fetch_patient_form'),
    # path('fetch_patient_form/<int:patient_id>/', views.fetch_patient_form, name='fetch_patient_form'),
    # path('save_patient/', views.save_patient, name='save_patient'),
    # path('save_patient/<int:patient_id>/', views.save_patient, name='save_patient_with_id'),
    
    # path('create_report/<int:patient_id>/', views.create_report_form, name='create_report_form'),
    # path('fetch_report/<int:report_id>/', views.fetch_report_form, name='fetch_report_form'),
    # path('save_report/', views.save_report, name='save_report'),
    # path('save_report/<int:report_id>/', views.save_report, name='save_report_with_id'),
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

    # path('add_polyp/<int:report_id>/', views.add_polyp, name='add_polyp'),
    # path('remove_polyp/<int:polyp_id>/', views.remove_polyp, name='remove_polyp'),

    # # Utils
    # path('get_available_segments/<int:colon_anatomy_id>/', views.get_available_segments, name='get_available_segments'),

    # # DB management
    # path('delete_all_entries/', views.delete_all_entries, name='delete_all_entries'),
    # path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),

    # Standard Django views
    # path('create_patient/', views.PatientCreateView.as_view(), name='create_patient'),
    # path('update_patient/<int:pk>/', views.PatientUpdateView.as_view(), name='update_patient'),
    # path('create_report/', views.ReportCreateView.as_view(), name='create_report'),
    # path('update_report/<int:pk>/', views.ReportUpdateView.as_view(), name='update_report'),
]
