from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import PostForm
from blog.models import Post, Comment
from .forms import CommentForm
from . import views
from django.http import HttpResponseRedirect
# Create your views here.
def create(request):  
    Data = {'Posts': Post.objects.all().order_by('-date')}
    if request.method == "POST":  
        form = PostForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return render(request, 'blog/blog.html', Data)
            except:  
                pass  
    else:  
        form = PostForm()  

    return render(request, 'blog/new.html', Data)

def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def edit(request, id):  
    post = Post.objects.get(id=id)  
    return render(request,'blog/edit.html', {'post':post})  

def update(request, id):  
    post = Post.objects.get(id=id)  
    form = PostForm(request.POST, instance = post)  
    if form.is_valid():  
        form.save()  
        return redirect("/blog")  

    return render(request,'blog/edit.html', {'post':post})  

def destroy(request, id):  
    post = Post.objects.get(id=id)  
    post.delete()  
    return redirect("/blog") 

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})