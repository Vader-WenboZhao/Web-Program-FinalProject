import time
import os

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Movie, Worker
from usersystem.models import Myuser, Review
from django.views.decorators import csrf


def homepage(request):
    from usersystem.views import current_user
    movie_workers = {}
    for movie in Movie.objects.all():
        a_list = []
        for a in movie.workers.all():
            a_list.append(a.name)
        movie_workers[movie.name] = a_list

    context = {
        "movies": Movie.objects.all(),
        "workers": Worker.objects.all(),
    }

    return render(request, "movies/homepage.html", context)


def all_movie(request):
    context = {
        "movies": Movie.objects.all(),
    }
    return render(request, "movies/movies.html", context)


def all_worker(request):
    context = {
        "workers": Worker.objects.all(),
    }
    return render(request, "workers/workers.html", context)


def movie(request, imdb_num):
    from usersystem.views import current_user
    try:
        movie = Movie.objects.get(imdb_num=imdb_num)
        actor_list = []
        for a in movie.workers.filter(work_type="actor"):
            actor_list.append(a)
        director = movie.workers.get(work_type="director").name
        reviews = movie.m_reviews.all()
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist.")
    nolike_users = Myuser.objects.exclude(likemovies=movie).all()
    nolike_list = []
    for user in nolike_users:
        nolike_list.append(user.username)
    can_like = False
    if current_user in nolike_list:
        can_like = True
    star_list = [1, 2, 3, 4, 5]
    imdb_link = "https://www.imdb.com/title/" + str(movie.imdb_num)
    img_link = "/static/pictures/" + str(movie.imdb_num) + ".jpg"
    able_like = True
    if current_user == "":
        able_like = False
    context = {
        "movie": movie,
        "actors": actor_list,
        "director": director,
        "reviews": reviews,
        "can_like": can_like,
        "star_list": star_list,
        "current_user": current_user,
        "imdb_link": imdb_link,
        "img_link": img_link,
        "able_like": able_like,
    }
    return render(request, "movies/movie.html", context)


def review(request, imdb_num):
    from usersystem.views import current_user
    try:
        review_txt = request.POST["review_txt"]
        star = int(request.POST["star"])
        movie = Movie.objects.get(imdb_num=imdb_num)
        user = Myuser.objects.get(username=current_user)
    except KeyError:
        return render(request, "movies/error.html", {"message: 没有选择电影"})
    except Myuser.DoesNotExist:
        return render(request, "movies/error.html", {"message: 请先登录"})
    except Movie.DoesNotExist:
        return render(request, "movies/error.html", {"message: 没有这个电影"})

    review_txt = review_txt + " - by " + current_user + " " + \
        str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    r = Review(review=review_txt, star=star, movie=movie, user=user)
    r.save()

    return HttpResponseRedirect(reverse("movie", args=(imdb_num,)))


def like_m(request, imdb_num):
    from usersystem.views import current_user
    try:
        like = 0
        like = request.POST["like"]
        movie = Movie.objects.get(imdb_num=imdb_num)
        user = Myuser.objects.get(username=current_user)
    except KeyError:
        return render(request, "movies/error.html", {"message: 没有选择电影"})
    except Myuser.DoesNotExist:
        return render(request, "movies/error.html", {"message: 请先登录"})
    except Movie.DoesNotExist:
        return render(request, "movies/error.html", {"message: 没有这个电影"})

    if like == "1":
        user.likemovies.add(movie)
    else:
        user.likemovies.remove(movie)

    return HttpResponseRedirect(reverse("movie", args=(imdb_num,)))


def worker(request, imdb_num):
    from usersystem.views import current_user
    try:
        worker = Worker.objects.filter(imdb_num=imdb_num).first()
        movie_list = []
        for a in worker.related_movie.all():
            movie_list.append(a)
    except Worker.DoesNotExist:
        raise Http404("Worker does not exist.")
    nolike_users = Myuser.objects.exclude(likeworkers=worker).all()
    nolike_list = []
    for user in nolike_users:
        nolike_list.append(user.username)
    can_like = False
    if current_user in nolike_list:
        can_like = True
    if worker.work_type == "actor":
        wt = "演员"
    elif worker.work_type == "director":
        wt = "导演"
    else:
        wt = "未知"
    imdb_link = "https://www.imdb.com/name/" + str(worker.imdb_num)
    img_link = "/static/pictures/" + str(imdb_num) + ".jpg"
    able_like = True
    if current_user == "":
        able_like = False
    context = {
        "worker": worker,
        "movies": movie_list,
        "can_like": can_like,
        "current_user": current_user,
        "imdb_link": imdb_link,
        "img_link": img_link,
        "work_type": wt,
        "able_like": able_like,
    }
    return render(request, "workers/worker.html", context)


def like_w(request, imdb_num):
    from usersystem.views import current_user
    try:
        like = 0
        like = request.POST["like"]
        worker = Worker.objects.filter(imdb_num=imdb_num).first()
        user = Myuser.objects.get(username=current_user)
    except KeyError:
        return render(request, "movies/error.html", {"message: 没有选择演职人员"})
    except Myuser.DoesNotExist:
        return render(request, "movies/error.html", {"message: 请先登录"})
    except Movie.DoesNotExist:
        return render(request, "movies/error.html", {"message: 没有这个演职人员"})

    if like == "1":
        user.likeworkers.add(worker)
    else:
        user.likeworkers.remove(worker)

    return HttpResponseRedirect(reverse("worker", args=(imdb_num,)))
