from django import forms
from django.shortcuts import render
from django.test import tag
from elasticsearch_dsl import Q
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from recepies.documnets import RecepyDocument
from django.core.mail import EmailMessage
from .forms import *


#pages 

#the search
def index(request): 

    query = request.GET.get('q')
    
    #if request.method == 'POST':
    #recepts = request.POST.getlist('tags')

    if query:
        q = Q(
            'bool',
            should = [
                Q('match',title = query),
                Q('match', ingredients = query),
                #Q('match', tags = recepts)
            ],
            minimum_should_match = 1)
        posts = RecepyDocument.search().query(q)
        #return render(request, 'index.html', {'posts':posts})
        #print (posts)
        
    else:
        posts = ""
       
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
    recepts = RecepyDocument.search().query() 
    return render(request, 'tags.html',{'posts':recepts})

def tag_template(request, tags):
    recepts =  RecepyDocument.search().query("match", tags=tags)
    return render(request, "tag_template.html", {"recepts": recepts, "tags": tags})

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm (request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            recipients = ['', ] #for email
            email_message = EmailMessage(name, message, email, recipients)
            email_message.send(fail_silently = False)
            

            return HttpResponseRedirect('./?submitted=True')
    else:
        form = ContactForm ()
        if submitted in request.GET:
            submitted = True

    recepts =  RecepyDocument.search().query()
    return render(request, 'contact.html', {'posts':recepts})

def about(request):
    recepts =  RecepyDocument.search().query()
    return render(request, 'about.html', {'posts':recepts})

def error404(request):
    return render(request, '404.html')

