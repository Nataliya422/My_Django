from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("Главная страница")

def catalog_posts(request):
    return HttpResponse("Каталог постов")

def post_detail(request, post_slug):
    return HttpResponse(f"Страница поста {post_slug}")

def catalog_categories(request):
    return HttpResponse("Каталог категорий")

def category_detail(request, category_slug):
    return HttpResponse(f"Страница категорий {category_slug}")

def catalog_tags(request):
    return HttpResponse("Каталог тегов")

def tag_detail(request, tag_slug):
    return HttpResponse(f"Страница тегай {tag_slug}")