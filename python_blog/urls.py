from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_posts, post_detail, catalog_categories, category_detail, catalog_tags, tag_detail  

urlpatterns = [
    path('', catalog_posts),
    path('<slug:post_slug>/', post_detail),

# Категории
    path('categories/', catalog_categories),
    path('categories/<slug:category_slug>/', category_detail),

# Тэги
    path('tags/', catalog_tags),
    path('tags/<slug:tag_slug>/', tag_detail),
    
]