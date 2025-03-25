from django.urls import path
from .views import PatientWizard,PatientListView,PatientUpdateView
from .forms import PatientIDForm, PatientAgeForm, PatientGenderForm, PatientDiagnosisForm, PatientKoumoku1Form

forms = [PatientIDForm, PatientAgeForm, PatientGenderForm, PatientDiagnosisForm,PatientKoumoku1Form]

urlpatterns = [
    path("wizard/", PatientWizard.as_view(forms), name="patient_wizard"),
    path("patient/", PatientListView.as_view(), name="patient_list"),
    path("patients/edit/<int:pk>/", PatientUpdateView.as_view(), name="patient_edit"),

]

