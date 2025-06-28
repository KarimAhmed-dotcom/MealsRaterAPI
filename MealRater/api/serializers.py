from rest_framework import serializers
from .models import *



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meal
        fields=['id','title','description']
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['id','stars','user','meal']
        

        
        
