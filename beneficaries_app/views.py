from django.shortcuts import render,redirect

from accounts.models import *
from beneficaries_app.forms import AssistanceRecordForm
from beneficaries_app.models import Assistance

# Create your views here.
def beneficarie_dashboard(request):
    return render(request,'beneficarytemp/index.html')

def view_volunteers_be(request):
    data = User.objects.filter(role=2)
    vol = UserProfile.objects.filter(user__in=data)
    return render(request, 'beneficarytemp/volunteer_view.html', {'vol': vol})

def view_welfareprograms(request):
    data = WelfareProgram.objects.all()
    return render(request,'beneficarytemp/view_welfare.html',{'data':data})

def add_assistance(request):
    if request.method == 'POST':
        form = AssistanceRecordForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.beneficiary = request.user
            form.save()
            return redirect('assistance-list')
    else:
        form = AssistanceRecordForm()
    return render(request, 'beneficarytemp/record_assistance.html', {'form': form})

def view_assistance(request):
    user=User.objects.get(username=request.user)
    data=Assistance.objects.all().filter(beneficiary_id=user.id)
    return render(request,'beneficarytemp/assistance.html',{'data':data})

