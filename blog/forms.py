from . models import BlogData
from django import forms
class Blogform(forms.ModelForm):
    class Meta:
        model=BlogData
        fields=['hedding','content','auther','date']