from django.contrib import admin

# Register your models here.
from .models import Post, Category  # Импортируйте необходимые модели

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'updated_date')  # Отображаемые поля в списке
    search_fields = ('title', 'content')  # Поля, по которым можно выполнять поиск
    prepopulated_fields = {'slug': ('title',)}  # Заполнение slug на основе заголовка

@admin.register(Category)  # Если вы хотите зарегистрировать и категорию
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Поля, которые вы хотите отображать в списке категорий
    prepopulated_fields = {'slug': ('name',)}