from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_data/',views.all_data,name = 'all_data'),
    path('search_title/',views.search_title,name = 'search'),
    path('search/',views.search_title_text,name = 'search'),
    #pages
    path('recipes/',views.all_recepies,name = 'recipes'),
    path('recipes/<str:title>',views.recipe_by_title,name = 'single_recipe_title'),
    # path('recepies2/',views.probe1,name = 'search'),
    path('tags/', views.tags, name = 'tags'),
    path('tag_template/', views.tag_template, name = 'tag_template'),
    #path('single_recipe/<str:title>/', views.single_recipe, name = 'single_recipe'),
    #path('single_recipe/<int:id>/', views.single_recipe, name = 'single_recipe'),
    path('single_recipe/<str:title>/', views.recipe_by_title, name = 'single_recipe_title'),
   
    path('single_recipe/', views.single_recipe, name = 'single_recipe'),
    
    path('index/', views.index, name = 'index'), #okey
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'), #okey
    path('error404/', views.error404, name = 'error404'),
]