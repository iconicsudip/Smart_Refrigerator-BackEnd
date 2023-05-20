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
    id = serializers.CharField()
    author_name = serializers.CharField(source='authorname')
    recipe_name = serializers.CharField(source='itemname')
    recipe_image = serializers.CharField(source='image')
    recipe_voted = serializers.BooleanField(source='isvoted')
    recipe_process =serializers.SerializerMethodField()
    ingredient =serializers.SerializerMethodField()
    vegetables =serializers.SerializerMethodField()
    author_image =serializers.SerializerMethodField()
    def get_recipe_process(self, obj):
        temp = obj.process
        if temp:
            return str(temp).split("//")
        else:
            return []
    
    def get_ingredient(self, obj):
        temp = obj.ingredient
        if temp:
            return str(temp).split("//")
        else:
            return []
    
    def get_vegetables(self, obj):
        temp = obj.vegetables
        if temp:
            return str(temp).split("//")
        else:
            return []
    
    def get_author_image(self,obj):
        valid_user = ValidUser.objects.get(username=obj.authorname)
        if valid_user:
            serializer = UserSerializer(valid_user)
            return serializer.data.get('image')
        else:
            return None

    class Meta:
        model = Recipe
        fields = ('id','author_name','recipe_name','recipe_process','ingredient','vegetables','videourl','votes','recipe_image','author_image','recipe_voted')

class FridgeSerialized(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        exclude = ('id', 'username')
