from django.urls import path

from . import views

urlpatterns = [
    path("avg-patient-waiting-time", views.avg_waiting_time_patient_data, name="api_avg_waiting_time_patient_data"),
    path("avg-waiting-time-dept-data", views.avg_waiting_time_dept_data, name="api_avg_waiting_time_dept_data"),
]