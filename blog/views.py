from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView
from django.views.generic.edit import CreateView,UpdateView
from . models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

# Create your views here.
class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_post.html"
    fields=['title','author','body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_edit.html"
    fields=['title','body']
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_delete.html"
    success_url=reverse_lazy('home')
