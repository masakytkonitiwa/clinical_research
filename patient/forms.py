from django import forms
from .models import Patient

class PatientIDForm(forms.Form):  # 旧 PatientNameForm
    patient_id = forms.IntegerField(label="患者ID")


class PatientAgeForm(forms.Form):
    age = forms.IntegerField(label="年齢")

class PatientGenderForm(forms.Form):
    gender = forms.ChoiceField(label="性別", choices=[("male", "男性"), ("female", "女性")])

class PatientDiagnosisForm(forms.Form):
    diagnosis = forms.CharField(label="診断内容", widget=forms.Textarea)

#項目ふやすときは以下
class PatientKoumoku1Form(forms.Form):
    koumoku1 = forms.CharField(label="項目1", widget=forms.Textarea)

class PatientForm(forms.ModelForm):
    class Meta:

        model = Patient
        fields = ["patient_id", "age", "gender", "diagnosis", "koumoku1"]  #項目ふやすときは左