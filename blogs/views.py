from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content']

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content']

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')