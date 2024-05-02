from django import forms
from beneficaries_app.models import Assistance

class AssistanceRecordForm(forms.ModelForm):
    assistance_type = forms.CharField(required=True)
    class Meta:
        model = Assistance
        fields = ['assistance_type', 'assistance_details','required_amount']

