from django.contrib import admin
from django.urls import path
from .views import CreateView, FetchView, MoveView

urlpatterns = [
    path('create/', CreateView, name='create_game'),
    path('fetch/<int:id>/', FetchView, name='fetch_game'),
    path('move/<int:id>/', MoveView, name='process_move'),
]