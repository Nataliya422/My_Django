
from django.contrib import admin
from django.urls import path
from python_blog.views import main
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),

# подключаем python_blog.urls
path('post/', include ('python_blog.urls')),
]