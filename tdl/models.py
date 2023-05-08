from django.db import models

# Create your models here.
class Task(models.Model):
    # member data 
    name = models.TextField()
    status = models.BooleanField()

    # method / function 
    def __str__(self):
        return str(self.id) + " " + self.name

class Grade(models.Model):
    name = models.CharField(max_length=2)

class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    grade = models.CharField(max_length=2) # A+ , A , B+ , B , C 
    # grade_id = models.IntegerField()
    result = models.BooleanField()
    marks = models.FloatField()

    def __str__(self):
        return str(self.id) + " " + self.name