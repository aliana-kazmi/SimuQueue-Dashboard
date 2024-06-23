from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('simulation-data', views.data_display, name='datatables'),
]