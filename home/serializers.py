from rest_framework import serializers
from .models import *
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # Now what fields do you want to serialize?
        # fields=['name', 'age'] #---if selective
        fields = '__all__' #all fields Serialize
        # exclude= ['name'] #add all fields but exclude the named ones