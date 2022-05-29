from django.shortcuts import render
from elasticsearch_dsl import Q
# Create your views here.
from django.http import HttpResponse
from recepies.documnets import RecepyDocument

#pages 

#the search
def index(request): 

    query = request.GET.get('q')

    if query:
        q = Q(
            'bool',
            should = [
                Q('match',title = query),
                Q('match', ingredients = query),
            ],
            minimum_should_match = 1)

        posts = RecepyDocument.search().query(q)
    else:
        posts = ''

    
    print (posts)
    return render(request, 'index.html', {'posts':posts})

#all data
def all_recepies(request):
    recepts = RecepyDocument.search().query() 
    return render(request, 'recipes.html',{'posts':recepts})

#result page
def recipe_by_title (request, title):

    recepts =  RecepyDocument.search().query("match", title=title)
    return render(request, "single_recipe.html", {"recepts": recepts})

#other
def tags(request):
    return render(request, 'tags.html')

def tag_template(request):
    return render(request, 'tag_template.html')

def contact(request):
    recepts =  RecepyDocument.search().query()
    return render(request, 'contact.html', {'posts':recepts})

def about(request):
    recepts =  RecepyDocument.search().query()
    return render(request, 'about.html', {'posts':recepts})

def error404(request):
    return render(request, '404.html')

