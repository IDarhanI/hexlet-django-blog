from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
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
        comment_form = ArticleCommentForm()
        
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
                "comment_form": comment_form,
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
            messages.error(
                request, 
                'Пожалуйста, исправьте ошибки в форме комментария'
            )
            return render(
                request,
                "articles/show.html",
                context={
                    "article": article,
                    "comment_form": comment_form,
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


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, 
            "articles/update.html", 
            {"form": form, "article_id": article_id}
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                f'Статья "{article.name}" успешно обновлена!'
            )
            return redirect('article:show', id=article_id)
        
        messages.error(
            request, 
            'Пожалуйста, исправьте ошибки в форме'
        )
        return render(
            request, 
            "articles/update.html", 
            {"form": form, "article_id": article_id}
        )


class ArticleDeleteView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = get_object_or_404(Article, id=article_id)
        return render(
            request,
            "articles/delete.html",
            {"article": article}
        )
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = get_object_or_404(Article, id=article_id)
        article_name = article.name
        
        try:
            # Удаляем статью
            article.delete()
            messages.success(
                request, 
                f'Статья "{article_name}" успешно удалена!'
            )
        except Exception as e:
            messages.error(
                request, 
                f'Произошла ошибка при удалении статьи: {str(e)}'
            )
            return redirect('article:show', id=article_id)
        
        return redirect('article:index')