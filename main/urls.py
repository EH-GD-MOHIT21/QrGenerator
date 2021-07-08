from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('generate',generate),
    path('decode',decode),
]