from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import *
from accounts.models import *
from accounts.forms import AssistanceForm
from beneficaries_app.models import Assistance


# Create your views here.
def index(request):
    return render(request, 'index.html')


def sign_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user.role == 1:
                    return redirect('admin-dashboard')
                elif user.role == 2:
                    return redirect('volunteer-dashboard')
                elif user.role == 3:
                    return redirect('beneficarie-dashboard')
                elif user.role == 4:
                    return redirect('donater-dashboard')
            else:
                messages.info(request, 'Invalid Credentials')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'login.html')


def sign_out(request):
    logout(request)
    return redirect('/')


def admin_dashboard(request):
    return render(request, 'admintemp/index.html')


def donater_dashboard(request):
    return render(request, 'donatertemp/index.html')


def add_volunteer(request):
    if request.method == 'POST':
        form = VolunteersForm(request.POST, request.FILES)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 2
            user.is_active = True
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            return redirect('view-volunteer')
    else:
        form = VolunteersForm()
        u_form = UserRegistrationForm()
    return render(request, 'admintemp/volunteer_register.html', {'form': form, 'u_form': u_form})


def add_fundraiser(request):
    if request.method == 'POST':
        form = FundraiserForm(request.POST)
        u_form = UserRegistrationForm(request.POST)
        if form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.role = 4
            user.is_active = True
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            return redirect('sign-in')
    else:
        form = FundraiserForm()
        u_form = UserRegistrationForm()
    return render(request, 'fundraiser_register.html', {'form': form, 'u_form': u_form})


def view_fundraisers(request):
    data = User.objects.filter(role=4)
    fr = UserProfile.objects.filter(user__in=data)
    print(fr)
    return render(request, 'admintemp/fundraiser_view.html', {'fr': fr})


def view_volunteers(request):
    data = User.objects.filter(role=2)
    vol = UserProfile.objects.filter(user__in=data)
    return render(request, 'admintemp/volunteer_view.html', {'vol': vol})


def update_volunteer(request, id):
    try:
        vol = UserProfile.objects.get(id=id)
    except UserProfile.DoesNotExist:
        return redirect(
            'view-volunteer')  # Assuming you have a view named 'view-volunteer' to redirect if the user doesn't exist

    if request.method == 'POST':
        form = VolunteersForm(request.POST, request.FILES, instance=vol)
        if form.is_valid():
            form.save()
            return redirect('view-volunteer')  # Redirect to some view after successful update
    else:
        form = VolunteersForm(instance=vol)
    return render(request, 'admintemp/update_volunteer.html', {'form': form})


def delete_volunteer(request, id):
    user_profile = get_object_or_404(UserProfile, id=id)
    if request.method == 'POST':
        user_profile.user.delete()
        user_profile.delete()
        return redirect('view_volunteers')

    return render(request, 'admintemp/delete_volunteer_confirmation.html', {'user_profile': user_profile})


def view_beneficaries_admin(request):
    data = User.objects.filter(role=3)
    bdata = UserProfile.objects.filter(user__in=data)
    return render(request, 'admintemp/beneficary_view.html', {'bdata': bdata})

def delete_beneficiaries(request, id):
    user_profile = get_object_or_404(UserProfile, id=id)
    if request.method == 'POST':
        user_profile.user.delete()
        user_profile.delete()
        return redirect('view-beneficary_ad')

    return render(request, 'admintemp/delete_beneficiaries_confirmation.html', {'user_profile': user_profile})



def add_welfareprograms(request):
    if request.method == 'POST':
        form = WelfareProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-welfareprograms')
    else:
        form = WelfareProgramForm()
    return render(request, 'admintemp/add_welfare.html', {'form': form})


def view_welfareprograms_ad(request):
    data = WelfareProgram.objects.all()
    return render(request, 'admintemp/view_welfare.html', {'data': data})


def assign_programs(request, pk):
    if request.method == 'POST':
        form = VolunteeringForm(request.POST)
        if form.is_valid():
            vol = WelfareProgram.objects.get(id=pk)
            vol.volunteer = form.cleaned_data['volunteer']
            vol.status = form.cleaned_data['status']
            vol.save()
            return redirect('view-welfareprograms-admin')
    else:
        form = VolunteeringForm()
    return render(request, 'admintemp/assign_programs.html', {'form': form})


def view_assistance_admin(request):
    data = Assistance.objects.all().order_by('-id')
    return render(request, 'admintemp/assistance.html', {'data': data})


def approve_assistance(request, pk):
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            data_x = Assistance.objects.get(id=pk)
            data_x.volunteer = form.cleaned_data['volunteer']
            data_x.save()
            return redirect('assistance-list-admin')
    else:
        form = AssistanceForm()
    return render(request, 'admintemp/assistance-list-admin.html', {'form': form})


def add_fund(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('view-fund')
    else:
        form = DonationForm()
    return render(request, 'donatertemp/add_fund.html', {'form': form})


def view_fund(request):
    data = Donation.objects.filter(user=request.user)
    return render(request, 'donatertemp/view_fund.html', {'data': data})


def view_donations(request):
    data = Donation.objects.all()
    return render(request, 'admintemp/view_donations.html', {'data': data})


def add_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-survey')
    else:
        form = SurveyForm()
    return render(request, 'admintemp/add_survey.html', {'form': form})


def view_survey(request):
    data = surveyquestions.objects.all()
    return render(request, 'admintemp/view_survey.html', {'data': data})


def sent_donations(request):
    total_donation_amount = Donation.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0

    data3_with_amounts = Assistance.objects.all()  # Retrieve all Assistance objects

    context = {
        'total_donation_amount': total_donation_amount,
        'data3_with_amounts': data3_with_amounts,
    }

    return render(request, 'admintemp/sent_donations.html', context)


# views.py
from django.db import transaction


from decimal import Decimal  # Add this line to import Decimal


def send_money_to_beneficiary(request, assistance_id):
    assistance = get_object_or_404(Assistance, pk=assistance_id)
    total_donation_amount = Donation.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or Decimal('0')

    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            required_amount = Decimal(assistance.required_amount)
            if 0 < amount <= required_amount:
                if amount <= total_donation_amount:
                    assistance.required_amount = str(required_amount - amount)
                    assistance.save()
                    # Update the total donation amount after money is sent
                    total_donation_amount -= amount
                    total_donation_amount = max(total_donation_amount, Decimal('0'))  # Ensure non-negative
                    messages.success(request, f"Successfully sent ${amount} to {assistance.beneficiary}.")
                else:
                    messages.error(request, "Not enough total donation amount available.")
            else:
                messages.error(request, "Invalid amount. Please enter a valid amount.")
        except ValueError:
            messages.error(request, "Invalid amount. Please enter a valid number.")
        else:
            # Redirect after processing POST request
            return redirect('sent_donations')

    # Calculate remaining total amount after processing POST request
    remaining_total_amount = total_donation_amount
    print("Remaining Total Amount:", remaining_total_amount)

    context = {
        'remaining_total_amount': remaining_total_amount,
        'total_donation_amount': total_donation_amount,
        'data3_with_amounts': Assistance.objects.all(),
    }

    return render(request, 'admin/sent_donations.html', context)


