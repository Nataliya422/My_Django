from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]
# Create your views here.
def main(request):
    return HttpResponse("Главная страница")

def catalog_posts(request):
    return HttpResponse("Каталог постов")

def post_detail(request, post_slug):
    return HttpResponse(f"Страница поста {post_slug}")

def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse('category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')
    
    return HttpResponse(f"""
        <h1>Каталог категорий</h1>
        {''.join(links)}
        <p><a href="{reverse('posts')}">К списку постов</a></p>
    """)


def category_detail(request, category_slug):
    category = [cat for cat in CATEGORIES if cat['slug'] == category_slug][0]
    
    if category:
        name = category['name']
    else:
        name = category_slug
        
    return HttpResponse(f"""
        <h1>Категория: {name}</h1>
        <p><a href="{reverse('categories')}">Назад к категориям</a></p>
    """)

def catalog_tags(request):
    return HttpResponse("Каталог тегов")

def tag_detail(request, tag_slug):
    return HttpResponse(f"Страница тега {tag_slug}")