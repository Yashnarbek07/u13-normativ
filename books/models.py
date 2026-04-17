from email.policy import default
from os.path import defpath
from random import choices

from django.db import models
from django.db.models import TextField
from django.forms import CharField, DecimalField, DateTimeField
from datetime import date


# Create your models here.

class BookType(models.TextChoices):
    STANDARD = "standard"
    ILMIY = "ilmiy"
    BADIIY = "badiiy"


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()

    def get_user_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age



    def __str__(self):
        return f"{self.first_name}, {self.last_name}"



class Author(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    class Meta:
        db_table = "authors"
        ordering = ["-date_of_birth"]

# title description author price type created_at
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ManyToManyField(Author, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length = 255, choices = BookType.choices, default = BookType.STANDARD)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"

    # CRUD -> INSERT, SELECT, UPDATE, DELETE

    """
    sql

    insert into authors (first_name, last_name, birth_date) VALUES ("sasas", "sasasa", "2024-2-1");

    SELECT * from authors;

    UPDATE authors SET first_name = ?, last_name = ?, birth_date = ? where id = ?;

    DELETE from authors where id = ?;
    """





    class Meta:
        db_table = 'books'
        ordering = ['-created_at']



