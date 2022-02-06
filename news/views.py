#from re import template
from django.views.generic import ListView, DetailView
#from matplotlib.style import context
from .models import *


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')


class NewsPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'