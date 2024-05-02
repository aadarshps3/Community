from django import forms
from accounts.models import *
from beneficaries_app.models import Assistance

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email','password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already in use')
        return username
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

LOCATIONS = (
    ('event planning', 'event planning'),
    ('fundraising', 'fundraising'),
    ('mentoring', 'mentoring'),
)

AVAILS = (
    ('full-time', 'full-time'),
    ('part-time', 'part-time'),
    ('weekends', 'weekends'),
)

class VolunteersForm(forms.ModelForm):
    name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    availability = forms.ChoiceField(choices=AVAILS, required=True)
    profile_picture = forms.ImageField(required=True)
    area = forms.CharField(required=True)
    class Meta:
        model = UserProfile
        fields = ['name', 'mobile_number','availability','profile_picture','area']

class FundraiserForm(forms.ModelForm):
    name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    class Meta:
        model = UserProfile
        fields = ['name', 'mobile_number']

class BeneficiariesForm(forms.ModelForm):
    name=forms.CharField(required=True)
    mobile_number=forms.CharField(required=True)
    area=forms.CharField(required=True)
    address=forms.Textarea()
    class Meta:
        model = UserProfile
        fields = ['name', 'mobile_number','area','address','description']

class WelfareProgramForm(forms.ModelForm):
     name=forms.CharField(required=True)
     venue=forms.CharField(required=True)
     class Meta:
        model = WelfareProgram
        fields = ['name','venue' ,'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

stat=(('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'))

class VolunteeringForm(forms.ModelForm):
    status=forms.ChoiceField(choices=stat,required=True)
    class Meta:
        model = WelfareProgram 
        fields = ['volunteer','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['volunteer'].queryset = User.objects.filter(role=2)

class AssistanceForm(forms.ModelForm):
    class Meta:
        model = Assistance 
        fields = ['volunteer','status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['volunteer'].queryset = User.objects.filter(role=2)

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donation_type','amount']

class SurveyForm(forms.ModelForm):
    class Meta:
        model = surveyquestions
        fields = ['question']


