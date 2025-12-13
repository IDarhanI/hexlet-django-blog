from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        # Используем пространство имен 'article'
        return redirect(reverse('article:index', kwargs={'tags': 'python', 'article_id': 42}))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


def about(request):
    from django.shortcuts import render
    return render(request, "about.html")