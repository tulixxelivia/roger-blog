from django import forms
from .models import Post
from .models import Subscription

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','location', 'text', 'img', )
class SubsForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name','email',)