from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=64)
    duration = models.IntegerField()
    type = models.CharField(max_length=128)
    country = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    imdb_num = models.CharField(max_length=256)
    date = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}({self.imdb_num})"


class Worker(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    birthday = models.CharField(max_length=64)
    english_name = models.CharField(max_length=64)
    imdb_num = models.CharField(max_length=256)
    work_type = models.CharField(max_length=32)
    related_movie = models.ManyToManyField(Movie, blank=True, related_name="workers")
    # related_movie = models.ForeignKey(
    #     Movie, on_delete=models.CASCADE, related_name="workers")

    def __str__(self):
        return f"{self.name}({self.imdb_num})"
