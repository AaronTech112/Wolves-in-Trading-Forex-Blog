from dataclasses import fields
from django.forms import ModelForm
from .models import Comment, User , Post

class CommentForm(ModelForm):
    class Meta:
      model = Comment
      fields = '__all__'
      exclude = ['post','avatar']

class UpdateAuthor(ModelForm):
  class Meta:
    model = User
    fields = ['profile','name','email']

class EditPost(ModelForm):
  class Meta:
    model = Post
    fields = ['image','title','subtitle','body','Links','LinkTitle','FinalQuote']

class UploadPost(ModelForm):
  class Meta:
    model = Post
    fields = ['image','title','subtitle','body','Links','LinkTitle','FinalQuote','category']