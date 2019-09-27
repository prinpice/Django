from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.id}: {self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=100,default='')
    audience = models.IntegerField()
    poster_url = models.TextField(default='')
    description = models.TextField(default='')
    genre = models.ForeignKey(Genre, on_delete=False)

    def __str__(self):
        return f'{self.id}: {self.title}'

class Score(models.Model):
    content = models.CharField(max_length=100, default='')
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.score}'
