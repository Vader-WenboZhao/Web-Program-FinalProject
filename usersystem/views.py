from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Myuser, Review
from wenbo_movie.models import Movie, Worker

last_search = ""
current_user = ""


def user(request):
    global current_user
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    current_user = request.user.username
    user = Myuser.objects.get(username=request.user.username)
    has_lm = True
    has_lw = True
    likemovies = user.likemovies.all()
    if len(likemovies) == 0:
        has_lm = False
    likeworkers = user.likeworkers.all()
    if len(likeworkers) == 0:
        has_lw = False
    # print(str(request.user))
    context = {
        "user": user,
        "likemovies": likemovies,
        "likeworkers": likeworkers,
        "has_lm": has_lm,
        "has_lw": has_lw,
    }
    return render(request, "users/user.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("user"))
    else:
        return render(request, "users/login.html", {"message": "不存在或密码错误"})


def logout_view(request):
    global current_user
    logout(request)
    current_user = ""
    return render(request, "users/login.html", {"message": "注销成功"})


def register_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    try:
        same_name_user = User.objects.get(username=username)
    except Exception:
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        new_myuser = Myuser.objects.create(
            d_user=new_user, username=username, password=password)
        new_myuser.save()
        return render(request, "users/login.html", {"message": "注册成功"})
    return render(request, "users/register.html", {"message": "已被注册"})


def register_jump(request):
    return render(request, "users/register.html", {"message": None})


def search_view(request):
    return render(request, "users/search.html", {"message": None})


def search(request):
    global last_search
    try:
        input = request.POST["input"]
    except Exception:
        input = last_search
    if input == "":
        return render(request, "users/search.html")
    last_search = input
    # Q(bread__gt=20)|Q(pk__lt=3)  name__contains=input
    has_m = True
    has_w = True
    workers = Worker.objects.filter(
        Q(name__contains=input) | Q(imdb_num__contains=input))
    movies = Movie.objects.filter(
        Q(name__contains=input) | Q(imdb_num__contains=input))
    if len(movies) == 0:
        has_m = False
    if len(workers) == 0:
        has_w = False
    context = {
        "has_w": has_w,
        "has_m": has_m,
        "workers": workers,
        "movies": movies,
    }
    return render(request, "users/search_result.html", context)
