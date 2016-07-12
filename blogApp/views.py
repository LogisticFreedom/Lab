#encoding=utf-8
from django.shortcuts import render,render_to_response
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog,Comment,Category,Tag,Info,MyUser
from .forms import CommentForms,WriteForm,InfoForm,RegisterForm,LoginForm


def getCkooie(request):
    username = request.COOKIES.get('username','')
    if username:
        username = '欢迎你！'+username
    else:
        username = 'nouser'
    return username

def getBlogs(request):
    username = getCkooie(request)
    ctx={'blogs':Blog.objects.all().order_by('-pubTime'),'username':username}
    return render(request,'home.html',ctx)

def getDetail(request,blog_id):
    username = getCkooie(request)
    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        raise Http404
    if request.method == 'GET':
        form = CommentForms()
    else:
        form = CommentForms(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data) # 创建一条评论记录
    ctx = {'blog':blog,'comments': blog.comment_set.all().order_by('-comTime'),'form': form,'username':username}
    return render(request,'details.html',ctx)

def showMembers(request):
    username = getCkooie(request)
    ctx = {'username':username}
    return render(request,'members.html',ctx)

def writeNewBlog(request):
    username = getCkooie(request)
    if username == 'nouser':
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'GET':
            form = WriteForm()
        else:
            form = WriteForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Blog.objects.create(**cleaned_data) # 创建一条博客记录
            # b = Blog(title=cleaned_data['title'])
            # b.author = cleaned_data['author']
            # b.content = cleaned_data['content']
            # b.category = cleaned_data['category']
            # b.tags = cleaned_data['tags']
            # b.save()
        ctx = {'form':form,'username':username}
        return render(request,'editor.html',ctx)


def login(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = MyUser.objects.filter(username__exact = username,password__exact = password)
        if user:
            #比较成功，跳转index
            response = HttpResponseRedirect('/control/')
            #将username写入浏览器cookie,失效时间为3600
            response.set_cookie('username',username,3600)
            return response
        else:
            #比较失败，还在login
            return HttpResponseRedirect('/online/login/')
    ctx = {'forms':form}
    return render(request,'login.html',ctx)

def video(request):
    username = getCkooie(request)
    ctx = {'username':username}
    return render(request,'video.html',ctx)

def info(request):
    username = getCkooie(request)
    if request.method == 'GET':
        form = InfoForm()
    else:
        form = InfoForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        Info.objects.create(**cleaned_data)
    ctx = {'form':form,'username':username}
    return render(request,'writeInfo.html',ctx)

def infoDisplay(request):
    username = getCkooie(request)
    ctx={'infos':Info.objects.all().order_by('-infoTime'),'username':username}
    return render(request,'info.html',ctx)

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        MyUser.objects.create(**cleaned_data)
    ctx = {'form':form}
    return render(request,'register.html',ctx)

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    return response

def control(request):
    username = getCkooie(request)
    if username == 'nouser':
        return HttpResponseRedirect('/login/')
    else:
        ctx = {'username':username}
        return render(request,'control.html',ctx)

def about(request):
    username = getCkooie(request)
    ctx = {'username':username}
    return render(request,'about.html',ctx)


# Create your views here.
