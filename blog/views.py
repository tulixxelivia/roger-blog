from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from .models import Subscription
from .forms import SubsForm
from .models import Events
from .forms import EventForm
from django.contrib import messages
#from django.core.paginator import Paginator
#from django.core.paginator import EmptyPage
#from django.core.paginator import PageNotAnInteger
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    limit = 2
#    paginator = Paginator(posts, limit)
#    page = request.GET.get('page')
#    try:
#        posts = paginator.page(page)
#    except PageNotAnInteger:
#        posts = paginator.page(1)
#    except EmptyPage:
#        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts':posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.img = request.FILES.get('img')
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.img=request.FILES.get('img')     
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def subscription_subs(request):
        if request.method == "POST":
                form = SubsForm(request.POST)
                if form.is_valid():
                        subscription = form.save(commit=False)
                        subscription.save()
                        messages.success(request,"Thank you for your Subscription!")
        else:
                form = SubsForm()
        return render(request, 'blog/subs.html',{'form': form})

def event_list(request):
        events= Events.objects.filter(event_date__lte=timezone.now()).order_by('-event_date')
        return render(request, 'blog/event_list.html', {'events':events})

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_list')
    else:
            form = EventForm()
    return render(request, 'blog/event_new.html', {'form': form})