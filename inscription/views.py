from django.shortcuts import render
# from .models import Inscription
from django.template.context_processors import request
from django.views.generic import ListView

# Create your views here.
from .models import Inscription, Intendant, Article


class ListeArticles(ListView, request):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "inscription/article_list.html"


def parent(request):
    return render(request, "")