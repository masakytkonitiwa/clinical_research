from django.urls import path
from .views import PatientWizard,PatientListView,PatientUpdateView
from .forms import PatientIDForm, PatientAgeForm, PatientGenderForm, PatientDiagnosisForm, PatientKoumoku1Form
from .views_example import run_migrations  # ← 追加

forms = [PatientIDForm, PatientAgeForm, PatientGenderForm, PatientDiagnosisForm,PatientKoumoku1Form]

urlpatterns = [
    path("wizard/", PatientWizard.as_view(forms), name="patient_wizard"),
    path("patient/", PatientListView.as_view(), name="patient_list"),
    path("patients/edit/<int:pk>/", PatientUpdateView.as_view(), name="patient_edit"),
    path('run-migrations/', run_migrations),  # ← 追加
]

