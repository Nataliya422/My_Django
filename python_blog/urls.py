
#python_blog\urls.py DJANGO APP python_blog

from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_posts, catalog_categories,  category_detail, catalog_tags, tag_detali, post_detali
from python_blog.views import main


urlpatterns = [
    # каталог постов posts/
    path('', catalog_posts, name='posts'),
    
    
    # Категории
    # Категории posts/categories/
    # Категории posts/categories/python/
    path('categories/', catalog_categories, name='categories'),
    path('categories/<slug:category_slug>/', category_detail, name='category_detail'),

    # Тэги posts/tags/
    # Тэги posts/tags/python/
    path('tags/', catalog_tags, name= 'tags'),
    path('tags/<slug:tag_slug>/', tag_detali, name= 'tag_detail'),

    # Посты posts/tags/
    path('<slug:post_slug>/', post_detali, name= 'post_detail'),
    

]