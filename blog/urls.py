
from django.contrib import admin
from django.urls import path
from python_blog.views import main
from django.urls import include


urlpatterns = [    
    path('admin/', admin.site.urls),
    path('', main, name='main'),  # Убедитесь, что имя маршрута указывается как строка
    # подключаем python_blog.urls
    path('posts/', include('python_blog.urls')),
]