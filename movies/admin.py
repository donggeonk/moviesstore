from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name', 'genre']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)