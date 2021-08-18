from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from owners.models import *

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(name=data['owner'], email=data['email'], age=data['owner_age'])
        return JsonResponse({'MESSAGE' : 'CREATED'}, status=201)


class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name=data['owner'])
        Dog.objects.create(owner = owner, name = data['dog_name'], age = data['dog_age'])
        return JsonResponse({'MESSAGE' : 'CREATED'}, status=201)


class OwnListView(View):
    def get(self, request):
        owners = Owner.objects.all()
        res = []
        for own in owners:
            dog_res = []
            dogs = own.dog_set.all()
            for dog in dogs:
                dog_res.append(
                        {
                            "name" : dog.name,
                            "age" : dog.age,
                        }
                )
            res.append(
                    {
                        "name" : own.name,
                        "email" : own.email,
                        "age" : own.age,
                        "dog_list" : dog_res,
                    }
            )
        return JsonResponse({'results' : res}, status = 200)


class DogListView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        res = []
        for dog in dogs:
            res.append(
                    {
                        "name" : dog.name,
                        "age" : dog.age,
                        "owner" : dog.owner.name,
                    }
            )
        return JsonResponse({'results' : res}, status = 200)
