from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'adult', 'backdrop_path', 'original_language', 'overview',
        'popularity', 'poster_path', 'released_date', 'title', 'vote_average',)


admin.site.register(Movie, MovieAdmin)
