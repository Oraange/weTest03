#from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from movies.models import *

class ActorView(View):
    def get(self, request):
        res = []
        actors = Actor.objects.all()
        for actor in actors:
            movies = list(actor.movie.values('title'))
            res.append(
                    {
                        "last_name" : actor.last_name,
                        "first_name" : actor.frist_name,
                        "movies" : movies
                    }
            )
        return JsonResponse({'results' : res}, status = 200)


class MovieView(View):
    def get(self,request):
        res = []
        movies = Movie.objects.all()
        for movie in movies:
            actor_res = []
            actors = movie.actor_set.all()
            for actor in actors:
                actor_res.append(
                        {
                            "name" : actor.frist_name,
                        }
                )
            res.append(
                    {
                        "movie name" : movie.title,
                        "running time" : movie.running_time,
                        "appearance" : actor_res,
                        }
                    )
        return JsonResponse({'results' : res}, status = 200)

