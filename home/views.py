from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import *
from home.serializers import PeopleSerializer
from django.shortcuts import render


# The `@api_view(['GET','POST'])` decorator in Django REST framework is used to create a view that can
# handle HTTP GET and POST requests. In this case, the `index` function is decorated with
# `@api_view(['GET','POST'])`, which means that this function can handle both GET and POST requests.
# When a GET request is made to the endpoint associated with this view, the function will execute the
# code block under the `elif request.method == 'GET':` condition. Similarly, when a POST request is
# made, the function will execute the code block under the `if request.method == 'POST':` condition.
@api_view(['GET','POST'])
def index(request):
    
    courses= {
        'name': 'Python',
        'learn': ['Flask','Django','Tornado'],
        'company': 'Youtube'
    }
    if  request.method == 'POST':
        print('POST Response')
        return Response(courses)
    elif request.method == 'GET':
        print(request.GET.get('search'))
        print('GET Response')
        # to accept data in the function:
        data= request.data
        print('****')
        print(data)
        print('****')
        return Response(courses)
    
# making the API to fill the model person and also get the persons from the model
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    objs=Person.objects.all() 

    if request.method =='GET':
        serializer= PeopleSerializer(objs, many=True)# many=true used as more than one object present in the QSet must be Serialized
        return Response(serializer.data)    
    elif request.method =='POST':
        dataH= request.data
        print(dataH)
        serializer=PeopleSerializer(data = dataH)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 
    
    elif request.method == 'PUT':
         dataH = request.data #FRONTEND SE AARAHA HAI---Dictionary form me aarha hai
         update_id= Person.objects.get(id=dataH['id'])
         serializer= PeopleSerializer(update_id ,data= dataH)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         
         return Response(serializer.errors)
    
    elif request.method == 'PATCH':
         dataH = request.data
         objs= Person.objects.get(id = dataH['id'])
         serializer = PeopleSerializer(objs, data= dataH , partial=True)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         
         return Response(serializer.errors)
    

   # This code block is handling the DELETE request for the `person` API.
    elif request.method == 'DELETE':
         dataH= request.data
         objs= Person.objects.all().filter(name__icontains='TEST')
         objs.delete()
         return Response({"message" : "Person's data is Deleted"})
#     filter(Rname__icontains =