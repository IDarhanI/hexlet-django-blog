from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleCommentForm, ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by('-created_at')[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        comment_form = ArticleCommentForm()  # Пустая форма для GET запроса
        
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
                "comment_form": comment_form,  # Убедитесь, что передаем форму
            },
        )
    
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        comment_form = ArticleCommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            
            messages.success(
                request, 
                'Ваш комментарий успешно добавлен!'
            )
            return redirect('article:show', id=article.id)
        else:
            # Если форма не валидна, показываем снова с ошибками
            return render(
                request,
                "articles/show.html",
                context={
                    "article": article,
                    "comment_form": comment_form,  # Форма с ошибками
                },
            )


def article_with_tags(request, tags, article_id):
    context = {
        'tags': tags,
        'article_id': article_id,
    }
    return render(request, 'articles/index.html', context)


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            messages.success(
                request, 
                f'Статья "{article.name}" успешно создана!'
            )
            return redirect('article:index')
        
        messages.error(
            request, 
            'Пожалуйста, исправьте ошибки в форме'
        )
        return render(request, 'articles/create.html', {'form': form})