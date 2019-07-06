from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name= 'post_detail' ),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('subscription/', views.subscription_subs, name='subscription_subs'),
    path('events/',views.event_list, name='event_list'),
    path('events/new/', views.event_new, name='event_new')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)