from django.shortcuts import render, redirect
from .models import PatientModel
from collections import defaultdict


# Create your views here.
def homepageview(request):
    patients = PatientModel.objects.all()
    dependency_dict = defaultdict(int)
    for patient in patients:
        dependency_dict[patient.dependents] = int(patient.dependents) * 3000

    context = {"patients": patients, "dependents": dependency_dict.items()}
    return render(request, "myapp/homepage.html", context)


def addpatientview(request):
    return render(request, "myapp/addpatient.html")


def addpatient(request):
    name = request.POST['name']
    age = request.POST['age']
    dependents = request.POST['dependents']
    address = request.POST['address']
    healthIssues = request.POST['healthIssues']
    PatientModel(name=name, age=age, dependents=dependents, address=address, healthIssues=healthIssues).save()
    return redirect('homepage')