from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            "title",
            "slug",
            "author",
            "body",
            "publish",
            "created",
            "updated",
            "status",
        ]