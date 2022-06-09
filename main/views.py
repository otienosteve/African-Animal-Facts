from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .serializer import AnimalSerializer
from .models import Animal
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import randint

@api_view(['GET'])
def home(request):
    animals=Animal.objects.all()
    animal=animals[randint(0,len(animals)-1)]

    anm=AnimalSerializer(animal,many=False)

    return Response(anm.data)

