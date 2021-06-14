from django.urls import path
from .views import *

urlpatterns = [
    path('', homepageview, name="homepage"),
    path('addpatient/', addpatientview, name="addpatientpage"),
    path('addpatient/save/', addpatient, name="addpatient"),

]