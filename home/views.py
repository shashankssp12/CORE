from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import *
from home.serializers import PeopleSerializer

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
    

    elif request.method == 'DELETE':
         dataH= request.data
         objs= Person.objects.all().filter(name__icontains='TEST')
         objs.delete()
         return Response({"message" : "Person's data is Deleted"})
#     filter(Rname__icontains =