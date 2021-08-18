from django.urls import path

from owners.views import *

urlpatterns = [
	path('owner', OwnerView.as_view()),
    path('dog', DogView.as_view()),
    path('ownerlist', OwnListView.as_view()),
    path('doglist', DogListView.as_view()),
]
