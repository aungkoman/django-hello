from django.db import models

# Create your models here.
class Author(models.Model):
    # member data
    name = models.CharField(max_length=20)
    town = models.CharField(max_length=20)

    # method
    def __str__(self):
        return str(self.id) + " " + self.name

class News(models.Model):
    # member data
    title = models.CharField(max_length = 200)
    description = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    # method
    def __str__(self):
        return str(self.id) + " " + self.title + " by " + self.author.name