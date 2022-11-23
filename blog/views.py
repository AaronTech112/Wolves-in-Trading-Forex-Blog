from logging import exception
from unicodedata import category, name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User,Post,Comment,Category
from django.db.models import Q
from .forms import CommentForm , UpdateAuthor, EditPost,UploadPost
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
import smtplib
from django.contrib.auth import authenticate , login , logout

def handling_404(request,exception):
    return render(request,'blog/404.html',{})

# Create your views here.import smtplib

def home(request):
    if request.method == "POST":
        user_email=request.POST.get('email')
        print(user_email)
    #     print(user_email)
    #     subject = 'Wolves Fx Blog'
    #     message = 'Thank for signing up'
    #     send_mail(subject, message, settings.EMAIL_HOST_USER, 
    #     [user_email])   
    #     return redirect('home')
        gmail_user = 'abdullahiaaron112@gmail.com'
        gmail_password = 'Aaronmosesdeboking1.'

        sent_from = gmail_user
        to = ['officialprojectsuccess@gmail.com', user_email]
        subject = 'OMG Super Important Message'
        body = 'wolves blog'

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print ('Email sent!')
        except:
            print ('Something went wrong...')


    category = Category.objects.all()
    cat_post=None
    q=''
    if request.GET.get('q') !=None: 
        q = request.GET.get('q') 
        cat_post=q
    else:
         ''

    post = Post.objects.filter(
        Q(category__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    ).order_by('?')[0:4]
    
    
    recent_post = Post.objects.all().order_by('created')
    
    context = {'post': post,'category':category,'recent_post':recent_post,'cat_post':cat_post}
    return render(request, 'blog/home.html',context)

def author_home(request):
    category = Category.objects.all()
    cat_post=None
    q=''
    if request.GET.get('q') !=None: 
        q = request.GET.get('q') 
        cat_post=q
    else:
         ''

    post = Post.objects.filter(
        Q(author__username__icontains=q)
    ).order_by('?')[0:4]
    
    
    recent_post = Post.objects.all().order_by('created')
    
    context = {'post': post,'category':category,'recent_post':recent_post,'cat_post':cat_post}
    return render(request, 'blog/home.html',context)
   
def next_home(request):
    category = Category.objects.all()
    cat_post=None
    q=''
    if request.GET.get('q') !=None: 
        q = request.GET.get('q') 
        cat_post=q
    else:
         ''

    post = Post.objects.filter(
        Q(category__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    ).order_by('?')[4:8]

    recent_post = Post.objects.all().order_by('created')
    
    context = {'post': post,'category':category,'recent_post':recent_post,'cat_post':cat_post}
    return render(request, 'blog/home.html',context)



def next2(request):
    category = Category.objects.all()
    cat_post=None
    q=''
    if request.GET.get('q') !=None: 
        q = request.GET.get('q') 
        cat_post=q
    else:
         ''

    post = Post.objects.filter(
        Q(category__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    ).order_by('?')[8:12]
    
    
    recent_post = Post.objects.all().order_by('created')
    
    context = {'post': post,'category':category,'recent_post':recent_post,'cat_post':cat_post}
    return render(request, 'blog/home.html',context)

def nextlast(request):
    category = Category.objects.all()
    cat_post=None
    q=''
    if request.GET.get('q') !=None: 
        q = request.GET.get('q') 
        cat_post=q
    else:
         ''

    post = Post.objects.filter(
        Q(category__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    ).order_by('?')[12:-0]
    
    
    recent_post = Post.objects.all().order_by('created')
    
    context = {'post': post,'category':category,'recent_post':recent_post,'cat_post':cat_post}
    return render(request, 'blog/home.html',context)

def single(request,pk):
    post = Post.objects.get(id=pk)
    category = Category.objects.all()
    comments = Comment.objects.filter(post=post)
    related_post = Post.objects.filter(category=post.category)[0:2]
    pk1=int(pk)
    nex , pre= pk1+1 , pk1-1
    next , previous = str(nex) , str(pre)

    try:
        next_post = Post.objects.get(id=next)
    except:
        next_post = Post.objects.get(id=previous)

    try:
        previous_post = Post.objects.get(id=previous)
    except:
        previous_post = Post.objects.get(id=next)

    form = CommentForm()
    if request.method == "POST":
        comment = Comment.objects.create(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            text = request.POST.get('text'),
            post = post
        )
        return redirect('single',pk=post.id)

    context = {
        'post': post, 
        'category':category, 
        'comments':comments,
        'form':form, 
        'related_post':related_post,
        'next_post': next_post,
        'previous_post': previous_post,
    }
    return render(request,'blog/single.html', context)


def author(request):
    authors0=User.objects.all()[0]
    authors1=User.objects.all()[1]
    authors2=User.objects.all()[2]
    authors3=User.objects.all()[3]

    posts=Post.objects.all()
    category = Category.objects.all()

    context = {
        'authors0':authors0,
        'authors1':authors1,
        'authors2':authors2,
        'authors3':authors3,
        'posts':posts,
        'category':category,
    }

    return render(request,'blog/author.html', context)


def contact(request):
    posts=Post.objects.all()
    category = Category.objects.all()
    context = {'category':category, 'posts': posts}
    return render(request,'blog/contact.html', context)

def about(request):
    posts=Post.objects.all()
    authors0=User.objects.all()[0]
    authors1=User.objects.all()[1]
    authors2=User.objects.all()[2]
    authors3=User.objects.all()[3]

    posts=Post.objects.all()
    category = Category.objects.all()

    context = {
        'authors0':authors0,
        'authors1':authors1,
        'authors2':authors2,
        'authors3':authors3,
        'posts':posts,
        'category':category,
    }

    return render(request,'blog/about.html', context)

def adminlogin(request):
    login_error1 = False
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email = email)
        except:
            login_error1 = True                    
        user = authenticate(request, username=email , password=password)
        
        if user is not None:
            login(request,user)
            return redirect('adminpage')
        else:
            login_error1 = True

    context = {'login_error1':login_error1}   
    return render(request,'adminlogin.html',context)

def adminpage(request):
    user = request.user
    author = User.objects.get(email=user.email)
    posts = Post.objects.filter(author=request.user).order_by('-created')
    form = UpdateAuthor(instance=user)
    if request.method == "POST":
        form = UpdateAuthor(request.POST,request.FILES,instance=user)
        if form.is_valid:
            form.save()
            return redirect('adminpage')
    context = {'author':author,'form':form, 'posts':posts}
    return render(request,'adminpage.html',context)

def editpost(request,pk):
    post=Post.objects.get(id=pk)
    form = EditPost(instance=post)
    if request.method == "POST":
        form = EditPost(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('adminpage')
    context={'form':form}
    return render(request,'editpost.html',context)

def uploadpost(request):
    form = UploadPost()
    if request.method == "POST":
        form = UploadPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('adminpage')
    context={'form':form}
    return render(request,'uploadpost.html',context)
    