from django import forms
from .models import Insurancerecord

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurancerecord
        fields = ('name','mobile','insurance_id','insurancename','email','insurancetype')
        labels = {
            'name':'Name',
            'mobile':'Mobile No.',
            'insurance_id':'Unique Insurance ID',
            'insurancename':'Policy Name',
            'email':'Email ID',
            'insurancetype':'Insurance Type'
        }

    def __init__(self, *args, **kwargs):
        super(InsuranceForm,self).__init__(*args, **kwargs)
        self.fields['insurancetype'].empty_label = "Select"
        self.fields['insurancetype'].required = False