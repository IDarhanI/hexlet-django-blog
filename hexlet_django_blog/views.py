from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        # Если нужно перенаправить на статью с тегами, используйте правильный именованный URL
        return redirect(reverse('article:article_with_tags', kwargs={'tags': 'python', 'article_id': 42}))
        # ИЛИ если нужно просто показать главную страницу без перенаправления:
        # return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


def about(request):
    from django.shortcuts import render
    return render(request, "about.html")