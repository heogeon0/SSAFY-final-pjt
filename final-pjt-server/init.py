import requests
import json


TMDB_API_KEY = 'f8b171aafccb0a97b02e46af402fb23f'

def get_movie_datas():
    total_data = []
    genres = [
    {
    "id": 28,
    "name": "Action"
    },
    {
    "id": 12,
    "name": "Adventure"
    },
    {
    "id": 16,
    "name": "Animation"
    },
    {
    "id": 35,
    "name": "Comedy"
    },
    {
    "id": 80,
    "name": "Crime"
    },
    {
    "id": 99,
    "name": "Documentary"
    },
    {
    "id": 18,
    "name": "Drama"
    },
    {
    "id": 10751,
    "name": "Family"
    },
    {
    "id": 14,
    "name": "Fantasy"
    },
    {
    "id": 36,
    "name": "History"
    },
    {
    "id": 27,
    "name": "Horror"
    },
    {
    "id": 10402,
    "name": "Music"
    },
    {
    "id": 9648,
    "name": "Mystery"
    },
    {
    "id": 10749,
    "name": "Romance"
    },
    {
    "id": 878,
    "name": "Science Fiction"
    },
    {
    "id": 10770,
    "name": "TV Movie"
    },
    {
    "id": 53,
    "name": "Thriller"
    },
    {
    "id": 10752,
    "name": "War"
    },
    {
    "id": 37,
    "name": "Western"
    }
    ]

    for i in range(1, 20):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        if i == 1:
            j = 0
            for movie in movies['results']:
                if j <= 10:
                    j += 1
                    if movie.get('release_date', ''):
                        if movie.get('backdrop_path', ''):
                            fields = {
                                'adult' : movie['adult'],
                                'backdrop_path' : movie['backdrop_path'],
                                'original_language' : movie['original_language'],
                                'overview' : movie['overview'],
                                'popularity': movie['popularity'],
                                'poster_path': movie['poster_path'],
                                'released_date': movie['release_date'],
                                'title': movie['title'],
                                'vote_average': movie['vote_average'],
                                'genres': movie['genre_ids'],
                                'is_active' : 1,
                                'director': '',
                                'actors': [],
                            }
                        for dic_moive in genres:
                            for i in range(len(fields.get('genres'))):
                                # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                                if dic_moive['id'] == fields.get('genres')[i]:
                                    fields.get('genres')[i] = dic_moive['name']

                        data = {
                            "pk": movie['id'],
                            "model": "movies.movie",
                            "fields": fields
                        }

                        total_data.append(data)
                else:
                    if movie.get('release_date', ''):
                        if movie.get('backdrop_path', ''):
                            fields = {
                                'adult' : movie['adult'],
                                'backdrop_path' : movie['backdrop_path'],
                                'original_language' : movie['original_language'],
                                'overview' : movie['overview'],
                                'popularity': movie['popularity'],
                                'poster_path': movie['poster_path'],
                                'released_date': movie['release_date'],
                                'title': movie['title'],
                                'vote_average': movie['vote_average'],
                                'genres': movie['genre_ids'],
                                'is_active' : 3,
                                'director': '',
                                'actors': [],
                            }
                        for dic_moive in genres:
                            for i in range(len(fields.get('genres'))):
                                # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                                if dic_moive['id'] == fields.get('genres')[i]:
                                    fields.get('genres')[i] = dic_moive['name']

                        data = {
                            "pk": movie['id'],
                            "model": "movies.movie",
                            "fields": fields
                        }

                        total_data.append(data)
        else:
            for movie in movies['results']:
                if movie.get('release_date', ''):
                    if movie.get('backdrop_path', ''):
                        fields = {
                            'adult' : movie['adult'],
                            'backdrop_path' : movie['backdrop_path'],
                            'original_language' : movie['original_language'],
                            'overview' : movie['overview'],
                            'popularity': movie['popularity'],
                            'poster_path': movie['poster_path'],
                            'released_date': movie['release_date'],
                            'title': movie['title'],
                            'vote_average': movie['vote_average'],
                            'genres': movie['genre_ids'],
                            'is_active' : 3,
                            'director': '',
                            'actors': [],
                        }
                    for dic_moive in genres:
                        for i in range(len(fields.get('genres'))):
                            # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                            if dic_moive['id'] == fields.get('genres')[i]:
                                fields.get('genres')[i] = dic_moive['name']


                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields
                    }

                    total_data.append(data)
    
    for i in range(1, 30):
        request_url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        if i == 1:
            j = 0
            for movie in movies['results']:
                if j <= 10:
                    j += 1
                    if movie.get('release_date', ''):
                        if movie.get('backdrop_path', ''):
                            fields = {
                                'adult' : movie['adult'],
                                'backdrop_path' : movie['backdrop_path'],
                                'original_language' : movie['original_language'],
                                'overview' : movie['overview'],
                                'popularity': movie['popularity'],
                                'poster_path': movie['poster_path'],
                                'released_date': movie['release_date'],
                                'title': movie['title'],
                                'vote_average': movie['vote_average'],
                                'genres': movie['genre_ids'],
                                'is_active' : 2,
                                'director': '',
                                'actors': [],
                            }
                        for dic_moive in genres:
                            for i in range(len(fields.get('genres'))):
                                # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                                if dic_moive['id'] == fields.get('genres')[i]:
                                    fields.get('genres')[i] = dic_moive['name']

                        data = {
                            "pk": movie['id'],
                            "model": "movies.movie",
                            "fields": fields
                        }

                        total_data.append(data)
                else:
                    if movie.get('release_date', ''):
                        if movie.get('backdrop_path', ''):
                            fields = {
                                'adult' : movie['adult'],
                                'backdrop_path' : movie['backdrop_path'],
                                'original_language' : movie['original_language'],
                                'overview' : movie['overview'],
                                'popularity': movie['popularity'],
                                'poster_path': movie['poster_path'],
                                'released_date': movie['release_date'],
                                'title': movie['title'],
                                'vote_average': movie['vote_average'],
                                'genres': movie['genre_ids'],
                                'is_active' : 3,
                                'director': '',
                                'actors': [],
                            }
                        for dic_moive in genres:
                            for i in range(len(fields.get('genres'))):
                                # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                                if dic_moive['id'] == fields.get('genres')[i]:
                                    fields.get('genres')[i] = dic_moive['name']

                        data = {
                            "pk": movie['id'],
                            "model": "movies.movie",
                            "fields": fields
                        }

                        total_data.append(data)
        else:
            for movie in movies['results']:
                if movie.get('release_date', ''):
                    if movie.get('backdrop_path', ''):
                        fields = {
                            'adult' : movie['adult'],
                            'backdrop_path' : movie['backdrop_path'],
                            'original_language' : movie['original_language'],
                            'overview' : movie['overview'],
                            'popularity': movie['popularity'],
                            'poster_path': movie['poster_path'],
                            'released_date': movie['release_date'],
                            'title': movie['title'],
                            'vote_average': movie['vote_average'],
                            'genres': movie['genre_ids'],
                            'is_active' : 3,
                            'director': '',
                            'actors': [],
                        }
                    for dic_moive in genres:
                        for i in range(len(fields.get('genres'))):
                            # 딕서너리 내에서 id 값이 같은 값들만 찾아 genre네임 확보
                            if dic_moive['id'] == fields.get('genres')[i]:
                                fields.get('genres')[i] = dic_moive['name']


                    data = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields
                    }

                    total_data.append(data)

    for data in total_data:
        movie_id = data['pk']
        
        credit_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}"
        credit_info = requests.get(credit_request_url).json()

        # 배우는 최대 10명까지만 저장한다.
        for cast in credit_info['cast'][:5]:
            data['fields']['actors'].append(cast['name'])
        
        if credit_info['crew']:
            data['fields']['director'] = credit_info['crew'][0]['name']
    
    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


get_movie_datas()
# get_genre_data()

'''
movies/fixtures/ 만들고 실행
장르부터 먼저 실행 주의

python manage.py loaddata genre_data.json
python manage.py loaddata movie_data.json

'''