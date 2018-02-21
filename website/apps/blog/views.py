from django.shortcuts import render
from .models import Category, Point, Article
from random import sample
# Create your views here.


def index(request):
    titles = Article.objects.select_related().all()
    length = len(titles)
    l1 = [x for x in range(1,length+1)]
    l2 = sample(l1, 6)
    subjects = []
    for i in l2:
        subjects.append(Article.objects.get(pk=i))
    context = {"subjects": subjects}
    # context = {"titles": titles}
    return render(request, 'blog/index.html', context)


def font(request):
    titles = Article.objects.filter(belong__link__category_name="前端").order_by('-add_time')
    context = {"titles": titles}
    return render(request, 'blog/font.html', context)


def back(request):
    titles = Article.objects.filter(belong__link__category_name="后端").order_by('-add_time')
    context = {"titles": titles}
    return render(request, 'blog/back.html', context)


def tools(request):
    titles = Article.objects.filter(belong__link__category_name="工具").order_by('-add_time')
    context = {"titles": titles}
    return render(request, 'blog/tools.html', context)


def content(request, title_id):
    title = Article.objects.get(pk=title_id)
    content = title.content
    add_time = title.add_time
    context = {"title": title, "content": content, "add_time": add_time}
    return render(request, 'blog/content.html', context)