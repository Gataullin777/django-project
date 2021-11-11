from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Theme, Relation


def articles_list(request):

    template = 'articles/news.html'

    data = Article.objects.order_by('-published_at').prefetch_related()
    relation_objs = Relation.objects.order_by('theme').prefetch_related()
    context = {
                'data': data,
               'relation_objs': relation_objs
               }

    return render(request, template, context)
