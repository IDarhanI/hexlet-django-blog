from hexlet_django_blog import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("about/", views.about),  # <- добавляем эту строчку
    path("admin/", admin.site.urls),
]