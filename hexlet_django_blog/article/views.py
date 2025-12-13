from django.views import View
from django.shortcuts import render


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'app_name': 'Articles',
        }
        return render(request, 'articles/index.html', context)
    
def index(request, tags, article_id):
    context = {
        'tags': tags,
        'article_id': article_id,
    }
    return render(request, 'articles/index.html', context)