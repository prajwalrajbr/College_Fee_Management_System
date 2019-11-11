from django import forms
from . import models

class create_stud_pd(forms.ModelForm):
    class Meta:
        model = models.Stud_PD
        fields = ['Sname','USN','Gender','DOB','POB','S_Pno','S_Add','Batch']


class create_stud_admn(forms.ModelForm):
    class Meta:
        model = models.Stud_Admn
        fields = ['Adm_No','Course','Adm_Year','Sem','Branch','Adm_Type','Quota']