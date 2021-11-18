from django.db import models

# Create your models here.


class BookEntry(models.Model):
    name = models.CharField(max_length=122)
    book = models.CharField(max_length=122)
    author = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name
    
# This is the models.py here we can create many tables this is responsible 
# to create table in our data base alsoit interects with serializer class
    

