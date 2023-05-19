from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from apis.models import Recipe,Fridge,ValidUser
# from apis.models import ValidUser


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    class Meta:
        model = ValidUser
        fields = ('id','username','email','name','image')
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
class FridgeSerialized(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        exclude = ('id', 'username')
