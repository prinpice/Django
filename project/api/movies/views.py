from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, MovieSerializer, ScoreSerializer
from .models import Genre, Movie

# Create your views here.

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre_movies = Movie.objects.filter(genre=genre_pk)
    serializer = MovieSerializer(genre_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def score_create(request, movie_pk):
    if request.method == "POST":
        print(request.data)
        # movie_id는 serializer에 object형태로 넣거나, save()에서 id=1 등으로 직접 넣어주면 된다.
        # commit=false 는 안됨
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"messages": "작성되었습니다."})