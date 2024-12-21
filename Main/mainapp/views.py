from django.http import HttpResponse
from django.shortcuts import render
from .models import Music
from django.shortcuts import render, redirect
from .models import make_password, Account
import json
from .script import process_audio_files

# Create your views here.


def main(request):
    template_name = 'mainapp/main.html'
    music = Music.objects.all()
    return render(request, template_name, {"music": music})


def play(request, id):
    template_name = 'mainapp/play.html'
    music = Music.objects.filter(id=id)
    return render(request, template_name, {"el": music[0]})

# account part


def create(request):
    template_name = "mainapp/create.html"
    if request.method == "POST":
        username = request.POST['username']
        if Account.objects.filter(username=username).exists():
            return render(request, template_name, {"error": "Username is already taken"})
        password = make_password(request.POST['password'])
        account = Account(username=username, password=password)
        account.save()
        user = Account.objects.filter(username=username)
        request.session[f"{account.id}"] = 'True'
        return redirect(f"/account/{user[0].id}")

    return render(request, template_name)


def login(request):
    template_name = "mainapp/login.html"

    if request.method == "POST":
        username = request.POST['username']
        password = make_password(request.POST['password'])

        if Account.objects.filter(username=username).exists():
            user = Account.objects.filter(username=username)

            if user[0].password == password:
                request.session[f"{user[0].id}"] = 'True'

                return redirect(f"/account/{user[0].id}")
            return render(request, template_name, {"error": "Password is not valid"})
        return render(request, template_name, {"error": "Username is not valid"})
    return render(request, template_name)


def account_main(request, id):
    template_name = 'mainapp/account_main.html'
    if request.session.get(f'{id}', False):
        music = Music.objects.all()
        if request.method == "POST":
            new_music = request.POST['music']
            account = Account.objects.filter(id=id)[0]
            favorite_music = Account.get_music(account.favorite_music)
            if len(favorite_music) == 0:
                favorite_music.append(new_music)
                account.favorite_music = Account.set_music(favorite_music)
                account.save()
                return render(request, template_name, {"music": music, "id": id})
            for el in favorite_music:
                if el == new_music:
                    return render(request, template_name, {"music": music, "id": id})
            favorite_music.append(new_music)
            account.favorite_music = Account.set_music(favorite_music)
            account.save()

        return render(request, template_name, {"music": music, "id": id})
    return redirect("/login")


def account_play(request, id, music_id):
    template_name = 'mainapp/account_play.html'
    if request.session.get(f'{id}', False):
        music = Music.objects.filter(id=music_id)
        if request.method == "POST":
            new_music = request.POST['music']
            account = Account.objects.filter(id=id)[0]
            favorite_music = Account.get_music(account.favorite_music)
            if len(favorite_music) == 0:
                favorite_music.append(new_music)
                account.favorite_music = Account.set_music(favorite_music)
                account.save()
                return render(request, template_name, {"el": music[0], "id": id})
            for el in favorite_music:
                if el == new_music:
                    return render(request, template_name, {"el": music[0], "id": id})
            favorite_music.append(new_music)
            account.favorite_music = Account.set_music(favorite_music)
            account.save()
        return render(request, template_name, {"el": music[0], "id": id})
    return redirect("/login")


def account_music(request, id):
    template_name = 'mainapp/account_music.html'
    if request.session.get(f'{id}', False):
        account = Account.objects.filter(id=id)[0]
        favorite_music = Account.get_music(account.favorite_music)
        music = Music.objects.filter(id__in=favorite_music)

        return render(request, template_name, {"music": music, "id": id})
    return redirect("/login")


def account_play_all(request, id):
    template_name = 'mainapp/account_play_all.html'
    if request.session.get(f'{id}', False):
        account = Account.objects.filter(id=id)[0]
        favorite_music = Account.get_music(account.favorite_music)
        music = Music.objects.filter(id__in=favorite_music)
        music_list = []
        for el in music:
            music_list.append({"title": el.title, "writer": el.writer, "cover": el.cover.url, "file": el.file.url})
        music_json = json.dumps(music_list)

        return render(request, template_name, {"music": music_json, "id": id})
    return redirect("/login")


