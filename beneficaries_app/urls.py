from django.urls import path
from beneficaries_app import views

urlpatterns = [
    path('beneficarie-dashboard/',views.beneficarie_dashboard,name='beneficarie-dashboard'),
    path('view-volunteers-be/',views.view_volunteers_be,name='view-volunteers-be'),
    path('view-welfareprograms/',views.view_welfareprograms,name='view-welfareprograms'),
    path('add-assistance/',views.add_assistance,name='add-assistance'),
    path('assistance-list/',views.view_assistance,name='assistance-list'),

]