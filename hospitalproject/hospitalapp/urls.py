from django.contrib import admin
from django.urls import path, include
from . import views

app_name="hospitalapp"

urlpatterns = [
    path('', views.index, name="index"),
    path("departments/", views.departments,name="departments"),
    path("doctors/", views.doctors,name="doctors"),
    path("departments_single/<int:hospital_id>", views.departmentsingle,name="departmentsingle"),

]
