from django import forms

from accounts.models import *
from beneficaries_app.models import Assistance

stat=(('Accepted','Accepted'),('On Duty','On Duty'),('Rejected','Rejected'))

class VolunteerStatusForm(forms.ModelForm):
    status=forms.ChoiceField(choices=stat,required=True)
    class Meta:
        model = WelfareProgram
        fields = ['status']
        
stat1=(('Approved','Approved'),('Rejected','Rejected'))
class AssistanceStatusForm(forms.ModelForm):
    status=forms.ChoiceField(choices=stat1,required=True)
    class Meta:
        model = Assistance
        fields = ['status']