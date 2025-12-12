from hexlet_django_blog import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("articles/", include("hexlet_django_blog.article.urls")),  # <- добавляем эту строчку
    path("admin/", admin.site.urls),
]
