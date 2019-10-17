from rest_framework import serializers
from .models import Movie, Farmer_board


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title_ko', 'title_en', 'open_year', 'genre', 'nation', 'director', 'description', 'poster_url',
                  'image_url']


class Farmer_boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_board
        fields = ['id', 'enroll_no', 'enroll_center', 'farm', 'crop', 'name', 'region', 'sort', 'crop_image',
                  'profile_image', 'followers', 'account']
        # followers 도 필드에 추가해야하는지??
