from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Meal(models.Model):
    title=models.CharField(max_length=32)
    description=models.TextField(max_length=360)
    
    
    def no_of_ratings(self):
        return len(Rating.objects.filter(meal=self))
    
    def avg_ratings(self):
        num_of_ratings=self.no_of_ratings()
        sum_of_ratings=0
        if len(Rating.objects.filter(meal=self)) :
            
            for i in Rating.objects.filter(meal=self) :
                sum_of_ratings+=i.stars
            return sum_of_ratings/num_of_ratings
        else:
            return 0
    
    def __str__(self):
        return self.title
    
class Rating(models.Model):
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE,related_name='ratings')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratings')
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    
    def __str__(self):
        return f"{self.stars}"
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['user','meal'],name='unique_user_meal_rating')
        ]
        indexes=[
            models.Index(fields=['user','meal'],name='user_meal_index_rating')
        ]