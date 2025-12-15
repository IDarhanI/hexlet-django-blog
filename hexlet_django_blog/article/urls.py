from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView, 
    ArticleView, 
    article_with_tags,
    ArticleFormCreateView
)

app_name = 'article'

urlpatterns = [
    path("<slug:tags>/<int:article_id>/", article_with_tags, name='article_with_tags'),
    path("", IndexView.as_view(), name='index'),
    path("<int:id>/", ArticleView.as_view(), name='show'),
    path("create/", ArticleFormCreateView.as_view(), name="create"),
]