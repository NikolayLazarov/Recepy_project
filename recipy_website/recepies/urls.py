from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name = 'index'), 
    
    path('recipes/',views.all_recepies,name = 'recipes'),
    path('recipes/<str:title>',views.recipe_by_title,name = 'single_recipe_title'),

    #path('single_recipe/', views.single_recipe, name = 'single_recipe'),
    path('single_recipe/<str:title>/', views.recipe_by_title, name = 'single_recipe_title'),
    
    path('tags/', views.tags, name = 'tags'),
    path('tag_template/', views.tag_template, name = 'tag_template'),
    
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'), 
    path('error404/', views.error404, name = 'error404'),
]