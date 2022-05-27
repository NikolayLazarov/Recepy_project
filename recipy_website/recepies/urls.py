from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_data/',views.all_data,name = 'all_data'),
    path('search_title/',views.search_title,name = 'search'),
    path('search/',views.search_title_text,name = 'search'),

]