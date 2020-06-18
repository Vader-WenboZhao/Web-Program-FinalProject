from django.contrib import admin

from .models import Movie, Worker
# Register your models here.

admin.site.register(Worker)
admin.site.register(Movie)
