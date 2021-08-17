#from django.shortcuts import render

# Create your views here.

import json

from django.http import JsonResponse
from django.views import View

from owner.models import *

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
           
