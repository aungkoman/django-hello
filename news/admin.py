from django.contrib import admin

# import our models
from .models import Author, News

# Register your models here
admin.site.register(Author)
admin.site.register(News)