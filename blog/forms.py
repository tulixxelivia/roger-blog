from django import forms
from .models import Post
from .models import Subscription
from .models import Events

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','location', 'text', 'img', )
class SubsForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name','email',)
class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('event_title','event_date','event_location','event_description',)
      
       