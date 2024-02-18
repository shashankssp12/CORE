from django.shortcuts import render
from .models import *
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from OncFlow.serializers import Patient_DataSerializer
# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def patient_register(request):
   objs=Patient_Data.objects.all()

   if request.method =='GET':
      serializer= Patient_DataSerializer(objs, many=True)# many=true used as more than one object present in the QSet must be Serialized
      return Response(serializer.data)    
   elif request.method =='POST':

         dataH= request.data
         print(dataH)
      #    data=request.POST///Why haven't  used this
         serializer=Patient_DataSerializer(data = dataH)
      #    Handle Full_name= first_name + last_name
      #         checking if the data is in the correct format, meets any required constraints.
         if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, # `status=status.HTTP_201_CREATED` is setting the
               status=status.HTTP_200_CREATED)
         return Response(serializer.errors) 
   elif request.method ==  'DELETE':
      Patient_Data.objects.all().delete()
      return Response({"message" : "Person's data is Deleted"})
   
    