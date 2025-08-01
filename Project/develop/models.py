from django.db import models

# Create your models here.


#Create model for table in mysql

class Student(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mob= models.CharField(max_length=10)

   
    
