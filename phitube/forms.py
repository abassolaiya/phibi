from django import forms
from . models import Comment, Phitube

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email', 'body', 'post',)


class PhitubeForm(forms.ModelForm):
    class Meta:
        model = Phitube
        fields = ('author', 'title', 'description', 'embeded_url', 'banner',)
