from django.db import models

# Create your models here.
class Task(models.Model):
    # member data 
    name = models.TextField()
    status = models.BooleanField()

    # method / function 
    def __str__(self):
        return str(self.id) + " " + self.name