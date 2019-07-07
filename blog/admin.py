from django.contrib import admin
from .models import Post
from .models import Subscription
from .models import Events

# Register your models here.

# Register the Post
admin.site.register(Post)
# Register the Subscription
class SubsAdmin(admin.ModelAdmin):
    list_display =('name','email')
    search_fields = ('name','email')
    fields = ('name','email')
admin.site.register(Subscription,SubsAdmin)

# Register the Events
admin.site.register(Events)