from django.urls import path
from .views import *

urlpatterns = [
    path('create/reporter/', CreateReporter, name="create-reporter"),
    path('', HomeReporter.as_view(), name="home-reporter"),
]