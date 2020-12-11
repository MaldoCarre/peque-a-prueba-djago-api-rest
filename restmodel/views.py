from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestModelSerializer
from.models import RestModel
# Create your views here.

#@api_view(['GET', 'POST']) #como estoy construyendo con funciones , tengo que usar estos decoradores para decirle que esto es un api view

@api_view(['GET'])
def jsonfunction (request):
    api_variable = {
        'nombre':'Jose',
        'apellido':'Maldonado',
    }
    return Response(api_variable)

@api_view(['GET'])
def lista(request):
    model = RestModel.objects.all()
    serializer = RestModelSerializer(model, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detalle(request,id):
    model = RestModel.objects.get(id=id)
    serializer = RestModelSerializer(model, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def carga (request):
    serializer = RestModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def editar (request,id):
    model = RestModel.objects.get(id=id)
    serializer = RestModelSerializer(instance=model,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def eliminar(request,id):
    model = RestModel.objects.get(id=id)
    model.delete()
    return Response('Objeto correctamente eliminado')
