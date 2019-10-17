from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, Farmer_boardSerializer
from .models import Movie, Farmer_board


# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie, many=True)
    print(serializer)
    print(dir(serializer))
    return Response(serializer.data)


@api_view(['GET'])
def farmer_list(request):
    farmers = Farmer_board.objects.all()
    serializer = Farmer_boardSerializer(farmers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def farmer_detail(request, farmer_id):
    farmer = get_object_or_404(Farmer_board, pk=farmer_id)
    serializer = Farmer_boardSerializer(farmer, many=True)
    print(serializer)
    print(dir(serializer))
    return Response(serializer.data)

# @api_view(['POST'])
# def sign_up(request):