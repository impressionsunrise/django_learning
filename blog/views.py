from django.shortcuts import render

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)

from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()
class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()
class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()
