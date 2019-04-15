from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'walkthrough/home.html', context)


def about(request):
    return render(request, 'walkthrough/about.html', {'title': 'About'})


def home_purchase(request):
    return render(request, 'walkthrough/home_purchase.html', {'title': 'Home Purchase'})


def marriage(request):
    return render(request, 'walkthrough/marriage.html', {'title': 'Marriage'})


def graduation(request):
    return render(request, 'walkthrough/graduation.html', {'title': 'Graduation'})


def general_one(request):
    return render(request, 'walkthrough/general_one.html', {'title': 'General One'})


def helpful(request):
    return render(request, 'walkthrough/helpful.html', {'title': 'Helpful'})
