from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', HomeView.as_view()),
]