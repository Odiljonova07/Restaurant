from django.urls import path
from .views import *


urlpatterns = [
    path('category/', category),
    path('foods/', food),
    path('reservation/', reservation),
]