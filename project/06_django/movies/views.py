from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all().order_by('-id')
    context = {
        'movies' : movies,
    }
    return render(request, 'index.html', context)
    
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie(title=title, audience=audience, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()    
    return redirect('detail', movie.id)
    
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie':movie,
    }
    return render(request, 'detail.html', context)
    
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'movie':movie,
    }
    return render(request, 'edit.html', context)
    
def update(request, movie_id):
    
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie.objects.get(id=movie_id)
    movie.title = title
    movie.audience = audience
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    
    movie.save()
    return redirect('detail', movie_id)
    
def delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('index')