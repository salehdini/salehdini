from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm , CommentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def index_view(request):
    posts=Post.objects.all()

    query=request.GET.get('q')
    if query:
        posts=posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query) 

        ).distinct()
    
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request,'post/index.html',{'posts':posts})

def create_view(request):

    if not request.user.is_authenticated:
        return Http404()
   
    form=PostForm(request.POST or None , request.FILES or None)
    if form.is_valid():
       post=form.save(commit=False)
       post.author=request.user
       post=form.save()
       messages.success(request,"POst created successfully",extra_tags='msg')
       return HttpResponseRedirect(post.get_absolute_url())
    context={
        'form':form
    }
    return render(request,'post/form.html',context)

def detail_view(request,id):
    post=get_object_or_404(Post,id=id)
    form=CommentForm(request.POST or None)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment=form.save()

    context={
        "post":post,
        "form":form
    }
    return render(request,'post/detail.html',context)
 
def update_view(request,id):

    if not request.user.is_authenticated:
        return Http404()

    if not request.user.is_authenticated:
        return Http404()

    post=get_object_or_404(Post,id=id)

    form=PostForm(request.POST or None, request.FILES or None , instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,"POst created successfully",extra_tags='msg')

        return HttpResponseRedirect(post.get_absolute_url()) 
    context={
        'form':form
    }
    return render(request,'post/form.html',context)

def delete_view(request,id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('post:index')