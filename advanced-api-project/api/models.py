# api/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Author's name")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
