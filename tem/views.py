from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'categories.html')    

def categories_food(request):
    return render(request, 'categories_food.html')     