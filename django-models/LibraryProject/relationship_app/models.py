from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    # Add other fields as needed

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    # Add other fields as needed

    def __str__(self):
        return self.name
