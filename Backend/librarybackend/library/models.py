from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.surname


class Book(models.Model):
    name = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=255)
    ISBN_code = models.CharField(max_length=255, unique=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
