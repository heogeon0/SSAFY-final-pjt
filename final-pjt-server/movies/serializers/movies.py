from rest_framework import serializers
from ..models import Movie
from .score import ScoreSerializer



class MovieSerializer(serializers.ModelSerializer):

    scores = ScoreSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ('pk', 'adult', 'backdrop_path', 'original_language', 'overview',
        'popularity', 'poster_path', 'released_date', 'title', 'vote_average', 'genres', 'actors', 'director', 'scores',)

class RecommandMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'poster_path', 'title',)