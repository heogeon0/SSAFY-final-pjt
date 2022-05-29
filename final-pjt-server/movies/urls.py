from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.movie),
    path('home/<int:movie_pk>/score/', views.create_score),
    path('home/<int:movie_pk>/score/<int:score_pk>/', views.score_update_or_delete),
    path('recommendation/', views.recommendation),
    path('searchmovie/', views.searchmovie)
    
]