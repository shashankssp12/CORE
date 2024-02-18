
from rest_framework import serializers
from .models import *

class Patient_DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient_Data
        fields = '__all__' #all fields Serialize