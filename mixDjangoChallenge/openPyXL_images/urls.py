from django.urls import path
from .views import *

urlpatterns = [
    path('create/reporter/xls', CreateReporter, name="create-reporter-xls")
]