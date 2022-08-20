from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getData(request):
    home = {'API':'Smart Refrigerator With Smart Cooking Techniques'}
    return Response(home)

@api_view(['GET'])
def register(request,email,password):
    person = {'name':'Sudip Das','email':email,'username':'sudip','password':password}
    return Response(person)