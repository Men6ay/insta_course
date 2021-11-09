from django import forms
from django.forms.models import inlineformset_factory
from django.shortcuts import render,redirect
from posts.models import Post,PostImage
from posts.forms import PostForm,PostImageForm
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})

def create(request):
    form = PostForm(request.POST or None)
    PostImageFormSet = inlineformset_factory(Post,PostImage,form=PostImageForm,extra=1)
    if request.method == 'POST':
        if form.is_valid():
            post = Post()
            post.text = form.cleaned_data['text']
            post.owner = request.user
            post.save()
            formset = PostImageFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()  
            return redirect('home')
    formset=PostImageFormSet()
    return render(request,'posts/create.html',locals())

def detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'posts/detail.html',{'post':post})

def update(request,id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post.text = form.cleaned_data['text']
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'posts/update.html',{'form':form})

def delete(request,id):
    if request.method =='POST':
        post= Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    return render(request,'posts/delete.html')

def get_profile(request,id):
    profile = User.objects.get(id=id)
    return render(request,'profile.html',{'profile':profile})
