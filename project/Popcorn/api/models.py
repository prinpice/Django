from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Farmer_board(models.Model):
    # id = models.IntegerField(primary_key=True)
    enroll_no = models.IntegerField()
    enroll_center = models.TextField()
    farm = models.TextField()
    crop = models.TextField()
    name = models.TextField()
    region = models.TextField()
    sort = models.IntegerField()
    crop_image = models.TextField(blank=True)
    profile_image = models.TextField(blank=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings", blank=True)


class User(AbstractUser):
    farmer = models.IntegerField(default=0)


class Farmer_review(models.Model):
    content = models.TextField()
    picture = models.ImageField(blank=True)
    star = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer_board, on_delete=models.CASCADE)


class Farmer_review_comment(models.Model):
    content = models.TextField()
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Farmer_review, on_delete=models.CASCADE)


class Movie(models.Model):
    title_ko = models.TextField(blank=True)
    title_en = models.TextField(blank=True)
    open_year = models.IntegerField(blank=True)
    genre = models.TextField(blank=True)
    nation = models.TextField(blank=True)
    director = models.TextField(blank=True)
    description = models.TextField(blank=True)
    poster_url = models.TextField(blank=True)
    image_url = models.TextField(blank=True)


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    review = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
