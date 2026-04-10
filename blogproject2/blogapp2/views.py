from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, UserRegisterForm   
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.filter(author=request.user).order_by('-created_at')

    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blogapp2/home.html', {'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blogapp2/signup.html', {'form': form})


def create_post(request):
    return HttpResponse("Create post")

def post_detail(request, id):
    return HttpResponse(f"Post {id}")
