from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from .models import Details, Categories

# Create your views here.
def index(request):
    neurology = Categories.objects.filter(department="Neurological Department")
    surgical = Categories.objects.filter(department="Surgical Department")
    dental = Categories.objects.filter(department="Dental Department")
    ophtha = Categories.objects.filter(department="Ophthalmological Department")
    return  render(request,"index.html", {"neurology":neurology, "surgical":surgical, "dental":dental, "ophtha":ophtha})



def departments(request):
    obj = Details.objects.all()
    doctorslist = Details.objects.all()
    return render(request, "departments.html", {"obj":obj, "doctorslist":doctorslist})


def doctors(request):
    doctors_list = Details.objects.all()
    return render(request,"doctor.html", {"doctors_list":doctors_list})


def departmentsingle(request, hospital_id):
    departmentsingle = Details.objects.filter(id=hospital_id)
    return render(request,"department-single.html", {"departmentsingle": departmentsingle})