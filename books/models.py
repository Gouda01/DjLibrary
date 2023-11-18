from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author (models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    biography = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,related_name='book_author',on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class Review (models.Model):
    book = models.ForeignKey(Book,related_name='book_review',on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return str(self.book)



# Create your models here.
