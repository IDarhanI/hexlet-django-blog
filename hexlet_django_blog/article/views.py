from django.shortcuts import render


def index(request):
    # Создаем контекст с данными для шаблона
    context = {
        'app_name': 'Articles',  # Название приложения для шаблона
    }
    
    # Используем шаблон из директории templates/articles
    return render(request, 'articles/index.html', context)