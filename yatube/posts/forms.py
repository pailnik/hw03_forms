from django import forms  # Импортируем модуль forms, из него возьмём класс ModelForm

from .models import Post  # Импортируем модель, чтобы связать с ней форму


'''class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ('text', 'group')'''


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {
            'group': 'группа',
            'text': 'пост',
        }

        fields = ('group', 'text')

