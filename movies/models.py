from django.db import models

# Create your models here.

class Actor(models.Model):
    frist_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    date_of_birth = models.DateField(auto_now = False, auto_now_add = False)
    movie = models.ManyToManyField('Movie')
    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length = 45)
    release_date = models.DateField(auto_now = False, auto_now_add = False)
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'



