from django.db import models

# Create your models here.
from wenbo_movie.models import Movie, Worker
from django.contrib.auth.models import User


class Myuser(models.Model):
    d_user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    likemovies = models.ManyToManyField(Movie, blank=True, related_name="liked_by_user")
    likeworkers = models.ManyToManyField(Worker, blank=True, related_name="liked_by_usr")
    def __str__(self):
        return f"Username: {self.username} Password: {self.password}, \n"

class Review(models.Model):
    review = models.CharField(max_length=4096)
    star = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, related_name="m_reviews")
    user = models.ForeignKey(Myuser, on_delete=models.DO_NOTHING, related_name="u_reviews")

    def __str__(self):
        return f"{self.review}({self.movie})"
