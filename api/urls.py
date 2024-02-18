from home.views import *
from OncFlow.views import *
from django.urls import path
# from django.conf.urls.static import static 
# from django.conf import settings

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('patient-registration/', patient_register)
]
