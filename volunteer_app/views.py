from django.shortcuts import render,redirect

from accounts.forms import *
from accounts.models import *
from volunteer_app.forms import *
from beneficaries_app.models import *

# Create your views here.
def volunteer_dashboard(request):
    return render(request,'vtrtemp/index.html')

def add_beneficary(request):
    if request.method == 'POST':
        form = BeneficiariesForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 3
            user.is_active = True
            user.save()
            print("work")
            data = form.save(commit=False)
            data.user = user
            data.save()
            print("workeee")
            return redirect('view-beneficary') 
    else:
        form = BeneficiariesForm()
        u_form = UserRegistrationForm()
    return render(request,'vtrtemp/beneficary_register.html',{'form':form,'u_form':u_form})

def view_beneficary(request):
    data = User.objects.filter(role=3)
    bdata = UserProfile.objects.filter(user__in=data)
    return render(request,'vtrtemp/beneficary_view.html',{'bdata':bdata})

def volunteering_assigned(request):
    vol=User.objects.get(username=request.user)
    data=WelfareProgram.objects.all().filter(volunteer=vol)
    return render(request,'vtrtemp/volunteer_assigned.html',{'data':data})

def update_volunteer_status(request,pk):
    if request.method=='POST':
        form=VolunteerStatusForm(request.POST)
        if form.is_valid():
            vol=WelfareProgram.objects.get(id=pk)
            vol.status=form.cleaned_data['status']
            vol.save()
            return redirect('volunteer-assigned')
    else:
        form=VolunteerStatusForm()
    return render(request,'vtrtemp/status_update.html',{'form':form})

def assistance_assigned(request):
    vol=User.objects.get(username=request.user)
    data=Assistance.objects.all().filter(volunteer=vol)
    return render(request,'vtrtemp/assistance.html',{'data':data})

def assistance_volunteer_status(request,pk):
    if request.method=='POST':
        form=AssistanceStatusForm(request.POST)
        if form.is_valid():
            vol=Assistance.objects.get(id=pk)
            vol.status=form.cleaned_data['status']
            vol.save()
            return redirect('assistance-assigned')
    else:
        form=AssistanceStatusForm()
    return render(request,'vtrtemp/assistance_update.html',{'form':form})

def view_survey_volunteer(request):
    data = surveyquestions.objects.all()
    return render(request,'vtrtemp/view_survey.html',{'data':data})
