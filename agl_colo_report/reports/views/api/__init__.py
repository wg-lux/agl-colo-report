from .patient_views import (
    PatientList,
    PatientCreateView,
    PatientAPIView,
)

from .patient import (
    get_patient,
    get_patients,
)

from .report_views import (
    ReportListCreateView,
    ReportRetrieveUpdateDestroyView,
)

from .polyp_views import (
    ColonPolypListCreateView,
    ColonPolypRetrieveUpdateDestroyView,
)
