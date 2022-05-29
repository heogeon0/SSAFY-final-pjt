from django.shortcuts import get_object_or_404
import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Score
from .serializers.movies import MovieSerializer, RecommandMovieSerializer
from .serializers.score import ScoreSerializer
from django.db.models import Q
import requests
import datetime
import random

# Create your views here.
@api_view(['GET'])
def movie(request):
    
    now = datetime.datetime.now().hour 
    if 5 <= now <= 10:
        time_idx = 0
    elif 11 <= now <= 16:
        time_idx = 1
    elif 17 <= now <= 22:
        time_idx = 2
    elif 23 <= now or now <= 4:
        time_idx = 3

    url = 'https://api.openweathermap.org/data/2.5/weather?lat=37&lon=126&appid=bc0f528e6e3d3bf21d81b9d6a5208af3'
    res = requests.get(url).json()
    weather = res.get('weather')[0].get('main')
    weather_list = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Atmosphere', 'Clear', 'Clouds']
    
    movie_genres_list = [["Horror", "Thriller"], ["Music", "Animation"], ["Crime", "Action"], ["Romance", "TV Movie"], ["Mystery", "Western"], ["Comedy", "Drama"], ["War", "Adventure"]]
    movie_time_list = ["Family", "History", "Fantasy", "Documentary"]
    idx = weather_list.index(weather)
    
    movies_time = Movie.objects.filter(genres__icontains=movie_time_list[time_idx]).order_by('-vote_average')[:10]
    
    movies_weather = Movie.objects.filter(Q(genres__icontains=movie_genres_list[idx][0]) | Q(genres__icontains=movie_genres_list[idx][1])).order_by('-popularity')[0:10]
    
    movies_now = Movie.objects.filter(is_active=1)
    
    movies_top10_popular = Movie.objects.filter(is_active=2)[:10]
    
    movies_korea_top10 = Movie.objects.filter(original_language='ko').order_by('-popularity')[:10]
    
    movies_animation = Movie.objects.filter(genres__icontains="Animation").order_by('-popularity')[:10]
    result = list(movies_now) + list(movies_weather) + list(movies_time) + list(movies_top10_popular) + list(movies_korea_top10) + list(movies_animation)
    serializer =  MovieSerializer(result, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_score(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.scores.filter(user=user).exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = ScoreSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

            scores = movie.scores.all()
            serializer = ScoreSerializer(scores, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def score_update_or_delete(request, movie_pk, score_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    score = get_object_or_404(Score, pk=score_pk)

    def update_score():
        if request.user == score.user:
            serializer = ScoreSerializer(score, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                scores = movie.scores.all()
                serializer = ScoreSerializer(scores, many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete_score():
        if request.user == score.user:
            score.delete()
            scores = movie.scores.all()
            serializer = ScoreSerializer(scores, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        return update_score()
    elif request.method == 'DELETE':
        return delete_score()

@api_view(['GET', 'POST'])
def recommendation(request):
    def get_movie():
        movies = Movie.objects.filter(vote_average__gt=5)
        sample_num = random.sample(range(0, len(movies)), 30)
        movies_list = []
        for i in sample_num:
            movies_list.append(movies[i])
        serializer = RecommandMovieSerializer(movies_list, many=True)
        return Response(serializer.data)

    def post_movie():
        movies = request.data['movie']
        movies_df = pd.read_csv("result.csv")
        genre_sim_sorted_ind = np.load('result.npy')
        def find_sim_movie(df, sorted_ind, title_name, top_n=10):
            title_movie = df[df['pk'] == title_name]
            title_index = title_movie.index.values

            similar_indexes = sorted_ind[title_index, : (top_n * 2)]
            similar_indexes = similar_indexes.reshape(-1)

            similar_indexes = similar_indexes[similar_indexes != title_index]

            return df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]
        similar_movies = find_sim_movie(movies_df, genre_sim_sorted_ind, movies[1], 10)
        for i in range(1, len(movies)):
            similar_movies.append(find_sim_movie(movies_df, genre_sim_sorted_ind, movies[i], 10))
        val = similar_movies[['pk']].values.tolist()
        random.shuffle(val)
        movie_list = []
        number_list = []
        i =0 
        while len(movie_list) != 6:
            if val[i][0] not in number_list:
                movie_list += list(Movie.objects.filter(pk=val[i][0]))
            i += 1
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)


    if request.method == 'GET':
        return get_movie()
    elif request.method == 'POST':
        return post_movie()

@api_view(['POST'])
def searchmovie(request):
    search_movies = Movie.objects.filter(title__icontains=request.data['keyword'])
    serializer = MovieSerializer(search_movies, many=True)
    return Response(serializer.data)