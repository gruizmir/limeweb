from django.forms import Form, ModelForm, CharField, EmailField, IntegerField, TextInput, Textarea, BooleanField, ImageField, ModelChoiceField, ValidationError,DecimalField
from django.db import models
from blog.models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(ModelForm):
    required_css_class = 'required'
    body = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Article
        exclude = ('author', 'creation_date', 'mod_date')
