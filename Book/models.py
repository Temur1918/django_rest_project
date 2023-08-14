from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title