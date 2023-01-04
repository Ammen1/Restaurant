
from django.urls import path

from.import views

app_name = 'tem'


urlpatterns = [
    path('', views.index, name='index'),
    path('categories', views.categories, name='categories'), 
    path('categories_food', views.categories_food, name='categories_food'), 
    #path('', views.index, name='index'),  
    
]