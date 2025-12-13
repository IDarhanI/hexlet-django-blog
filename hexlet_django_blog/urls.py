from hexlet_django_blog import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("about/", views.about, name='about'),
    path("articles/", include("hexlet_django_blog.article.urls")),
    path("admin/", admin.site.urls),
]