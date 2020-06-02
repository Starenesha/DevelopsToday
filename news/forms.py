from django import forms
from .models import Comment, Author


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'author': forms.CheckboxSelectMultiple(),
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'] = forms.ModelChoiceField(queryset=Author.objects.all())
