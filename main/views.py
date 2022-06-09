from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .serializer import AnimalSerializer
from .models import Animal
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view,renderer_classes
from random import randint

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def home(request):
    animals=Animal.objects.all()
    animal=animals[randint(0,len(animals)-1)]

    anm=AnimalSerializer(animal,many=False)

    return Response(anm.data)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def all(request):
    animals=Animal.objects.all()
    
    anm=AnimalSerializer(animals,many=True)

    return Response(anm.data)

@api_view(['POST'])
def update(request):
    serialinst=AnimalSerializer(data=request.data)
    if serialinst.is_valid():
        serialinst.save()
    return Response(serialinst.data)


