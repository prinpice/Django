from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    scores = movie.score_set.all()
    context = {
        'movie': movie,
        'scores': scores,
    }
    return render(request, 'movies/detail.html', context)

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:movie_list')
    else:
        return redirect('movies:movie_detail', movie.id)

def score_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        score = Score()
        score.content = request.POST.get('content')
        score.movie = movie
        score.score = request.POST.get('score')
        score.save()
    return redirect('movies:movie_detail', movie.id)

def score_delete(request, movie_id, score_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
    return redirect('movies:movie_detail', movie.id)

