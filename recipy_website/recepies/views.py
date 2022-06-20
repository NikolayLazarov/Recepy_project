from django.shortcuts import render
from elasticsearch_dsl import Q
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from recepies.documnets import RecepyDocument

from django.core.mail import EmailMessage
from .forms import ContactForm

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

def filters(request):
    filter = request.GET.get('f')

    if filter:
        f = Q(
            'bool',
            should = [
                Q('match', tags = filter),
            ],
            minimum_should_match = 1)

        posts = RecepyDocument.search().query(f)
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

def recipe_by_filter (request, tags):

    recepts =  RecepyDocument.search().query("match", tags=tags)
    return render(request, "single_recipe.html", {"recepts": recepts})

#other
def tags(request):
    return render(request, 'tags.html')

def tag_template(request):
    return render(request, 'tag_template.html')

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm (request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['', ] # Enter at least 1 recipient (You may need to add email to "Authorized Recipients" (Sending -> Overview))
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

