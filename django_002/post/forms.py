from django import forms
from .models import Post
class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable'}))
    
        
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'