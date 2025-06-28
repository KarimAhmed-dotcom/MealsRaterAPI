from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Meal(models.Model):
    title=models.CharField(max_length=32)
    description=models.TextField(max_length=360)
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE,related_name='ratings')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    
    def __str__(self):
        return self.meal.title
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['user','meal'],name='unique_user_meal_rating')
        ]
        indexes=[
            models.Index(fields=['user','meal'],name='user_meal_index_rating')
        ]