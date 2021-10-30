from django import forms
from django.db.models import fields
from django.forms import widgets
from posts.models import Post,PostImage

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text']

class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image':forms.ClearableFileInput(attrs={
                'class':'form-control-file'
            })
        }