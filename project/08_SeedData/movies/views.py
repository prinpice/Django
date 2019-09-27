from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import MovieModelForm, ScoreModelForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/list.html', context)
    
def new(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_list')
    else:
        form = MovieModelForm()
        return render(request, 'movies/form.html', {'form':form,})
        
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    scores = movie.score_set.all()
    context = {
        'movie':movie,
        'scores':scores,
    }
    return render(request, 'movies/detail.html', context)
    
    
def edit(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "POST":
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.id)
    else:
        form = MovieModelForm(instance=movie)
        return render(request, 'movies/form.html', {'form':form,})
    
    
def score_new(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        score = Score()
        score.content = request.POST.get('content')
        score.movie = movie
        score.score = request.POST.get('score')
        score.save()
    return redirect('movies:detail', movie.id)
    
def score_delete(request, movie_id, score_id):
    movie = get_object_or_404(Movie, id=movie_id)
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
    return redirect('movies:detail', movie.id)