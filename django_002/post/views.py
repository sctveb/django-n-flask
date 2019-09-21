from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm, PostModelForm
from .models import Post
# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request,"post/list.html",{'posts':posts})
    
def create(request):
    if request.method == "POST":
        # 저장로직
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            # title = form.cleand_data.get('title')
            content = form.cleaned_data['content']
            Post.objects.create(title=title,content=content)
            
            return redirect(resolve_url('post:list'))
        pass
    else:
        # 입력할 수 있는 폼 리턴
        form = PostForm()
        return render(request,"post/create.html", {'form':form})
        
def detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post/detail.html',{'post':post})
    
def update(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            content = form.cleaned_data.get('content') 
            # post.update(title=title,content=content)
            post.title = title
            post.content = content
            post.save()
            return redirect(resolve_url('post:detail',id))
    else:
        form = PostForm({'title':post.title,'content':post.content})
        return render(request,'post/update.html',{'form':form,'post':post})
    
def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(resolve_url('post:list'))
    

def model_create(request):
    if request.method == "POST":
        # 저장하는 로직
        pass
    else:
        # 폼을 보여주는 로직
        form = PostModelForm()
        return render(request,'post/model_create.html',{'form':form})
    
def model_update(request,id):
    pass