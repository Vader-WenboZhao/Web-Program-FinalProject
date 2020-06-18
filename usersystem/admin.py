from django.contrib import admin

from .models import Myuser, Review
from wenbo_movie.models import Movie, Worker
# Register your models here.

admin.site.register(Myuser)
admin.site.register(Review)
