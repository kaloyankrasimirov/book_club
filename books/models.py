from django.db import models
from django.utils.text import slugify

from templates_exercise.models import TimeStampModel


class Book(TimeStampModel):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction', 'Fiction',
        NON_FICTION = 'Non-Fiction', 'Non-Fiction',
        FANTASY = 'Fantasy', 'Fantasy',
        SCIENCE = 'Science', 'Science',
        HISTORY = 'History', 'History',
        MYSTERY = 'Mystery', 'Mystery'


    title = models.CharField(
        unique=True,
        max_length=50
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    isbn = models.CharField(
        max_length=12,
        unique=True
    )
    genre = models.CharField(
        max_length=50,
        choices=GenreChoices.choices,
    )
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False
    )
    pages = models.CharField(
        max_length=100,
    )
    publisher = models.CharField(
        max_length=100
    )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")

        super().save(*args, **kwargs)

class Tags(models.Model):
    name = models.CharField(
        max_length=50,
    )

    books = models.ManyToManyField(Book)

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name