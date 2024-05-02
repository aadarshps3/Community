from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign-in/',views.sign_in,name='sign-in'),
    path('sign-out/',views.sign_out,name='sign-out'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('donater-dashboard',views.donater_dashboard,name='donater-dashboard'),
    path('add-volunteer/',views.add_volunteer,name='add-volunteer'),
    path('view-volunteer/',views.view_volunteers,name='view-volunteer'),
    path('update_volunteer/<int:id>/',views.update_volunteer,name='update_volunteer'),
    path('delete_volunteer/<int:id>/',views.delete_volunteer,name='delete_volunteer'),
    path('delete_beneficiaries/<int:id>/',views.delete_beneficiaries,name='delete_beneficiaries'),
    path('add_fundraiser/',views.add_fundraiser,name='add_fundraiser'),
    path('view-fundraiser/',views.view_fundraisers,name='view-fundraiser'),
    path('view-beneficary_ad/',views.view_beneficaries_admin,name='view-beneficary_ad'),
    path('add-welfareprograms/',views.add_welfareprograms,name='add-welfareprograms'),
    path('view-welfareprograms-admin/',views.view_welfareprograms_ad,name='view-welfareprograms-admin'),
    path('assign-programs/<int:pk>/',views.assign_programs,name='assign-programs'),
    path('assistance-list-admin/',views.view_assistance_admin,name='assistance-list-admin'),
    path('assistance-list-approve/<int:pk>/',views.approve_assistance,name='assistance-list-approve'),
    path('view-donations',views.view_donations,name='view-donations'),
    path('add-survey',views.add_survey,name='add-survey'),
    path('view-survey',views.view_survey,name='view-survey'),
    path('sent_donations',views.sent_donations,name='sent_donations'),




    path('add-fund',views.add_fund,name='add-fund'),
    path('view-fund',views.view_fund,name='view-fund'),
    path('send-money/<int:assistance_id>/', views.send_money_to_beneficiary, name='send_money'),




]