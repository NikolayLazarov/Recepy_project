from django.shortcuts import render
from elasticsearch_dsl import Q
# Create your views here.
from django.http import HttpResponse
from recepies.documnets import RecepyDocument


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def search_title(request):
    query = request.GET.get('q')

    if query:
        q = Q(
            'multi_match',
            query = query,
            fields = [
                'title'
            ]
        )

        posts = RecepyDocument.search().query(q)
        response = posts.execute()
    else:
        posts = ''

    return render(request, 'search.html',{'posts':posts})


def all_data(request):
    recepts =  RecepyDocument.search().query()
    # cars =  CarDocument.search().query("match", title = "AUDI")
    #                                        'for the html': from here
    return render(request, 'all_data.html',{'posts':recepts})


def search_title_text(request):
    query = request.GET.get('q')

    if query:
        q = Q(
            'bool',
            # must = [
            #     Q('match', name = query),
            # ],
            # must_not = [],
            should = [
                Q('match',title = query),
                Q('match', ingredients = query),
                # Q('match', color = query),

            ],
            minimum_should_match = 1)

        posts = RecepyDocument.search().query(q)
        # response = posts.execute()
    else:
        posts = ''

    return render(request, 'search.html',{'posts':posts})