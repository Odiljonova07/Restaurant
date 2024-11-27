from django.urls import path
from app.backoffice.views import *

urlpatterns = [
    path('', dashboard, name = 'dashboard-url'),
    path('categories/', category_view, name = 'categories-url'),
    path('category_create/', category_create, name = 'category-create-url'),
    path('category_update/<int:pk>/', category_update, name = 'category-update-url'),
    path('category_delete/<int:pk>/', category_delete, name = 'category-delete-url'),
]