from django.shortcuts import render, redirect
from .models import *


def delete_subject(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/subjects/")


def subjects(request):
    if request.method == 'POST':
        Fan.objects.create(
            nom=request.POST.get("nom"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish")),
            asosiy=request.POST.get("asosiy") == "on"
        )
        return redirect("/subjects/")

    word = request.GET.get("search_word")
    result = Fan.objects.all()
    if word:
        result = result.filter(nom__contains=word)
    content = {
        "subjects": result,
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, 'subjects.html', content)


def direction(request):
    if request.method == 'POST':
        Yonalish.objects.create(
            nom=request.POST.get("nom"),
            aktiv=request.POST.get("aktiv") == "on"
        )

    content = {
        "direction": Yonalish.objects.all()
    }
    return render(request, 'direction.html', content)


def delete_dir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/direction/")


def teachers(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan"))
        )
        return redirect("/teachers/")

    jinsi = [jins[0] for jins in JINS]
    word = request.GET.get("search_word")
    result = Ustoz.objects.all()
    if word:
        result = result.filter(ism__contains=word)
    content = {
        "teachers": result,
        "jins": jinsi,
        "fanlar": Fan.objects.all()
    }
    return render(request, 'teachers.html', content)
