from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.id}: {self.name}'
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.id}: {self.title[:20]}'
        
        
class Score(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}:{self.content[:20]}'