from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/list.html', context)
    
    
# TODO: 평점 max, min제어필요
def detail(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    score_form = ScoreForm()
    context = {
        'movie' : movie,
        'score_form': score_form,
    }
    return render(request, 'movies/detail.html', context)
    
    
@login_required
@require_POST
def score_create(request, movie_id):
    form = ScoreForm(request.POST)
    if form.is_valid():
        score = form.save(commit=False)
        score.user = request.user
        score.movie_id = movie_id
        score.save()
    else:
        return redirect('movies:list')
    return redirect('movies:detail', movie_id)
    
@login_required
def score_delete(request, movie_id, score_id):
    score = Score.objects.get(pk=score_id)
    if score.user == request.user:
        score.delete()
    return redirect('movies:detail', movie_id)