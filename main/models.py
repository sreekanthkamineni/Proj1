from django.db import models

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    photo= models.ImageField(upload_to='photos/%y/%m/%d')
    is_breakfast = models.BooleanField(default=True)
    is_lunch = models.BooleanField(default=True)
    is_dinner = models.BooleanField(default=True)
    is_drinks = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
