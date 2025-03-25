from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from .models import Patient
from .forms import  PatientForm 


from django.views.generic import ListView,UpdateView


class PatientWizard(SessionWizardView):
    template_name = "patient/form_wizard.html"
    
    def get_form_initial(self, step):
        return self.storage.get_step_data(step) or {}


    def done(self, form_list, **kwargs):
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        Patient.objects.create(
            patient_id=data["patient_id"],  # `patient_id` を保存
            age=data["age"],
            gender=data["gender"],
            diagnosis=data["diagnosis"],
            #項目ふやすときは以下
            koumoku1=data["koumoku1"],
            
        )

        return render(self.request, "patient/done.html", {"data": data})



class PatientListView(ListView):
    model = Patient
    template_name = "patient/patient_list.html"
    context_object_name = "patients"

    def get_queryset(self):
        return Patient.objects.all().order_by('-created_at')  # 最新順


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "patient/patient_edit.html"
    success_url = reverse_lazy("patient_list")  # 編集完了後に患者リストへリダイレクト
        
    def get_object(self, queryset=None):
        pk_value = int(self.kwargs["pk"])
        print(f"DEBUG: 確認のため受け取った pk={pk_value}")
        return Patient.objects.get(pk=pk_value)
