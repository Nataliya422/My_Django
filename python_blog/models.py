from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
    """
    Модель поста
    """
    STATUS_CHOICES = [
        ("draft", "Черновик"),
        ("review", "На проверке"),
        ("reviewed", "Проверено"),
        ("published", "Опубликовано"),
    ]

    title = models.CharField(max_length=200, unique=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="Слаг")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор")
    data = models.JSONField(null=True, blank=True, default=dict, verbose_name="Дополнительные данные")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")  # Удален default
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft", verbose_name="Статус")

    def __str__(self):
        """Возвращает строковое представление поста."""
        return self.title

    def get_absolute_url(self):
        """Возвращает абсолютный URL поста по его slug."""
        return reverse("blog:post_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        """Переопределение метода save для автоматической генерации slug."""
        if not self.slug:
            self.slug = slugify(self.title)  # Убедитесь, что slugify работает с корректным импортом
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Tag(models.Model):
    """Модель для тегов."""
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")

    def __str__(self):
        """Возвращает строковое представление тега."""
        return self.name

    def get_absolute_url(self):
        """Возвращает абсолютный URL тега по его slug."""
        return reverse("blog:tag_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        """Переопределение метода save для автоматической генерации slug."""
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

class Category(models.Model):
    """Модель для категорий."""
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")
    description = models.TextField(blank=True, null=True, default="Без описания", verbose_name="Описание")

    def __str__(self):
        """Возвращает строковое представление категории."""
        return self.name

    def get_absolute_url(self):
        """Возвращает абсолютный URL категории по ее slug."""
        return reverse("blog:category_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        """Переопределение метода save для автоматической генерации slug."""
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]