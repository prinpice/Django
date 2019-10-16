from rest_framework import serializers
from .models import Genre, Movie, Score

# serializer : query set, model instance 등의 복잡한 데이터를 JSON, XML 등의 content type으로 쉽게 변환 가능한 python datatype으로 변환시켜줌

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', ]

class  MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre', ]

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score', 'movie', ]