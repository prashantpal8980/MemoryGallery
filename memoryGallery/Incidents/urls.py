from django.urls import path
from . import views


urlpatterns = [
    path('',views.IncidentSeenHere,name='IncidentSeenHere'),
    path('create/',views.IncidentCreated,name='IncidentCreated'),
    path('<int:incident_id>/edit/',views.IncidentEdited,name='IncidentEdited'),
    path('<int:incident_id>/delete/',views.incident_delete,name='IncidentDelete'),
    path('register',views.register,name='register'),
    
    
    
] 