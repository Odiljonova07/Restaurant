from django.shortcuts import render, redirect
from app.models import *


def dashboard(request):
    return render(request, 'index.html')


def category_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name = name)
        return redirect('categories-url')


def category_update(request, pk):
    if request.method == 'POST':
        category = Category.objects.get(id=pk)
        category.name = request.POST.get('name')
        category.save()        
        return redirect('categories-url')


def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories-url')