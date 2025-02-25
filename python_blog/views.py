from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .blog_data import dataset

from.models import Post, Category


CATEGORIES = [
    {"slug": "python", "name": "Python"},
    {"slug": "django", "name": "Django"},
    {"slug": "postgresql", "name": "PostgreSQL"},
    {"slug": "docker", "name": "Docker"},
    {"slug": "linux", "name": "Linux"},
]

def main(request):
    catalog_categories_url = reverse("blog:categories")  # Получаем URL для каталога категорий
    catalog_tags_url = reverse("blog:tags")              # Получаем URL для каталога тегов

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
        "active_page": "main",
    }
    return render(request, "main.html", context)

def about(request):
    context = {
        "title": "О нас",
        "text": "Текст страницы о нас",
        "active_page": "about",
    }
    return render(request, "about.html", context)

def catalog_posts(request):
    posts = Post.objects.all()  # Получаем все посты
    context = {"title": "Блог", "posts": posts}
    return render(request, "blog.html", context)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)  # Получаем пост по slug
    context = {"title": post.title, "post": post}
    return render(request, "post_detail.html", context)

from .models import Post, Category

def catalog_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories, "title": "Категории блога"}
    return render(request, "catalog_categories.html", context)

def category_detail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    # Используем related_name="posts" для получения всех постов категории
    posts = category.posts.all()
    context = {
        "category": category,
        "posts": posts,
        "title": f"Категория: {category.name}",
    }
    return render(request, "category_detail.html", context)

def catalog_tags(request):
    return HttpResponse("Каталог тегов")  # Здесь можно позже реализовать логику для каталога тегов

def tag_detail(request, tag_slug):
    return HttpResponse(f"Страница тега {tag_slug}")  # Здесь можно позже реализовать логику для деталей тега