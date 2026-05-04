from django.contrib import admin
from .models import Movie
# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','director','description','collections','budget']
    list_display_links=['director','name']

