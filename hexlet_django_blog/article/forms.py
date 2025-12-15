from django import forms
from .models import Article, ArticleComment


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Введите ваш комментарий здесь...'
            }),
        }
        labels = {
            'content': 'Ваш комментарий',
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите название статьи'
            }),
            'body': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': 'Введите содержание статьи...'
            }),
        }
        labels = {
            'name': 'Название статьи',
            'body': 'Содержание статьи',
        }