from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def news(reguest):
    news = Post.objects.order_by('-date_posted')
    paginator = Paginator(news, 3)
    page = reguest.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(reguest, 'osnova/news.html', {'page': page,  'posts': posts})


class dinamicStranits(DetailView):
    model = Post
    template_name = 'osnova/statiea.html'
    context_object_name = 'Post'
