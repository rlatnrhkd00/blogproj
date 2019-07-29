from django import forms
from .models import Blog, Portfolio

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

class PortPost(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'image', 'description']

#class BlogPost(forms.Form):
#    email = forms.EmailField()
#    files = forms.FileField()
#    url = forms.URLField()
#    words = forms.CharField(max_length=200)
#    max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])