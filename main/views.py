from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .serializer import AnimalSerializer
from .models import Animal
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from random import choice
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def home(request):
    animals=Animal.objects.raw('SELECT * FROM main_animal order by random()')
    animal=choice(animals)

    anm=AnimalSerializer(animal,many=False)

    return Response(anm.data)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def all(request):
    animals=Animal.objects.all()
    
    anm=AnimalSerializer(animals,many=True)

    return Response(anm.data)


@api_view(['POST'])
@csrf_exempt
def update(request):
    serialinst=AnimalSerializer(data=request.data)
    if serialinst.is_valid():
        serialinst.save()
    return Response(serialinst.data)

def desc(request):
    return render(request,'index.html')



from django.db import connection
from .models import Animal
def results(request):
    cursor = connection.cursor()
    cursor.execute('''select *customer
order by random()
limit 5;''')


#Access Control- 
# GET
# GET ALL endpoint
#POST->protect

