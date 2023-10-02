from .patient_views import (
    PatientList,
    PatientCreateView,
    PatientAPIView,
    PatientListTableView
)

from .patient import (
    get_patient,
    get_patients,
)

from .report_views import (
    CreateReportAPIView,
    ReportListTableView,
    ReportListCreateView,
    ReportRetrieveUpdateDestroyView,
    GetReportAPIView,
    UpdateReportAPIView,
)

from .polyp_views import (
    ColonPolypListCreateView,
    ColonPolypRetrieveUpdateDestroyView,
    CreateColonPolypAPIView,
)
