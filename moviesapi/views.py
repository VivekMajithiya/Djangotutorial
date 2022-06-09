from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Movies

# Create your views here.
class Another(View):

    movies = Movies.objects.all()
    # print(type(movies))
    output = ''
    for movie in movies:
        output += f'Movie {movie.title} is available for booking now <br>'

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First demo output from movie api')
