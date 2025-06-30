from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer
    
    @action(detail=True,methods=['post'])
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            
            meal=Meal.objects.get(id=pk)
            stars=request.data['stars']
            username=request.data['username']
            user=User.objects.get(username=username)
            
            
            try:
                #update
                rate=Rating.objects.get(user=user.id,meal=meal.id)
                rate.stars=stars
                rate.save()
                serializer=RatingSerializer(rate)
                json={
                    'message':'Meal Rate Updated',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
                
            except :
                #create
                rating=Rating.objects.create(user=user,meal=meal,stars=stars)
                rating.save()
                serializer=RatingSerializer(rating)
                json={
                    'message':'Meal Rate Created',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
        else:
            json={
                'message':'starts not provided'
            }
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer