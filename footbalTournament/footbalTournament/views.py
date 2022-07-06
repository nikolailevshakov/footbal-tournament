from django.shortcuts import render


def home_view(request):
    return render(request, "index.html")


def game_view(request):
    return render(request, "game.html")


def history_view(request):
    return render(request, "history.html")


def memes_view(request):
    return render(request, "memes.html")


def season_view(request):
    return render(request, "season.html")