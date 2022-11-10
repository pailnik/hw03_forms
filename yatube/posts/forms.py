from django import forms

from .models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        labels = {
            'group': 'группа',
            'text': 'пост',
        }

        fields = ('group', 'text')
