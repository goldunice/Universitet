from django.shortcuts import render, redirect
from .models import *


def delete_subject(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/subjects/")


def subjects(request):
    word = request.GET.get("search_word")
    result = Fan.objects.all()
    if word:
        result = result.filter(nom__contains=word)
    content = {
        "subjects": result
    }
    return render(request, 'subjects.html', content)


def direction(request):
    content = {
        "direction": Yonalish.objects.all()
    }
    return render(request, 'direction.html', content)


def delete_dir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/direction/")


def teachers(request):
    word = request.GET.get("search_word")
    result = Ustoz.objects.all()
    if word:
        result = result.filter(ism__contains=word)
    content = {
        "teachers": result
    }
    return render(request, 'teachers.html', content)
