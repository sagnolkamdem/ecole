from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic import ListView
from .models import Inscription, Intendant, Article


urlpatterns = [
    # url(r'^$', ListView.as_view(model=Article,)),
    url(r'^$', views.ListeArticles.as_view(), name="blog_liste"),
    # path('accueil/', views.home, name='home'),
    path('inscrire/', views.parent, name='parent'),

]