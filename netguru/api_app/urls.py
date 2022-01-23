from django.urls import path, include
from . views import *
app_name = 'api_app'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/rating/<int:pk>/', CarRatingView.as_view()),
    path('car/list/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarsDetailView.as_view()),
]