from django.db import models

# Create your models here.
class Task(models.Model):
    # member data
    name = models.TextField()
    status = models.BooleanField()

    # methods
    def __str__(self):
        return self.name + " | " + str(self.status) 