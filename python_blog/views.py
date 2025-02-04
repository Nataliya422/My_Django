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

MENU_ITEMS = [
    {"title": "Главная", "url_name": "main"},
    {"title": "Все посты", "url_name": "blog:posts"},
    {"title": "Категории", "url_name": "blog:categories"},
    {"title": "Теги", "url_name": "blog:tags"},
]
 
# Create your views here.
def main(request):
    catalog_categories_url = reverse("blog:categories")
    catalog_tags_url = reverse("blog:tags")

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_statusr": "admin",
        "menu_items": MENU_ITEMS,
    }
    return render(request, "main.html", context)

def catalog_posts(request):
    return HttpResponse("Каталог постов")

def post_detail(request, post_slug):
    return HttpResponse(f"Страница поста {post_slug}")

def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse("blog:category_detail", args=
        [category["slug"]])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')
    return HttpResponse(
        f"""
        <h1>Каталог категорий</h1>
        {''.join(links)}
        <p><a href="{reverse("blog:posts")}">К списку постов</a></p>
    """
    )

def category_detail(request, category_slug):
    category = [cat for cat in CATEGORIES if
    cat["slug"] == category_slug][0]

    if category:
        name = category["name"]
    else:
        name = category_slug
    
    context = {
        "title": f"Категория: {name}",
        "text": f"Текст категории {name}",
    }
    return render(request, "category_detail.html", context)

def catalog_tags(request):
    return HttpResponse("Каталог тегов")

def tag_detail(request, tag_slug):
    return HttpResponse(f"Страница тега {tag_slug}")

