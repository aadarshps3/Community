from django.urls import path
from volunteer_app import views

urlpatterns = [
    path('volunteer-dashboard/',views.volunteer_dashboard,name='volunteer-dashboard'),
    path('add-beneficary/',views.add_beneficary,name='add-beneficary'),
    path('view-beneficary/',views.view_beneficary,name='view-beneficary'),
    path('volunteer-assigned/',views.volunteering_assigned,name='volunteer-assigned'),
    path('assistance-assigned/',views.assistance_assigned,name='assistance-assigned'),
    path('update-volunteer-status/<int:pk>/',views.update_volunteer_status,name='update-volunteer-status'),
    path('assistance-volunteer-status/<int:pk>/',views.assistance_volunteer_status,name='assistance-volunteer-status'),
    path('view_survey_volunteer',views.view_survey_volunteer,name='view_survey_volunteer'),


]