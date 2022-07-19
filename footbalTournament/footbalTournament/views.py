from django.shortcuts import render
from datetime import datetime


def home_view(request):
    return render(request, "index.html")


def game_view(request):
    return render(request, "game.html")


def history_view(request):
    return render(request, "history.html")


def memes_view(request):
    return render(request, "memes.html")


def season_view(request):
    home_teams = ['Спартак1', 'Спартак2', 'Спартак3', 'Спартак4', 'Спартак5',
                  'Спартак6', 'Спартак7', 'Спартак8', 'Спартак9', 'Спартак0']
    guest_teams = ['Локомотив1', 'Локомотив2', 'Локомотив3', 'Локомотив4', 'Локомотив5',
                   'Локомотив6', 'Локомотив7', 'Локомотив8', 'Локомотив9', 'Локомотив0']
    season_end = datetime.strptime('Oct 1 2022', '%b %d %Y')

    #'name': [очки в сезоне, очки за месяц, очки за неделю]
    users = {'Левшаков': [0, 1, 0], 'Титов': [3, 4, 0], 'Пасюк': [6, 8, 0], 'Рыкованов': [9, 8, 0]}
    ctx = {'weekend_dates': '12, 13 июля', 'season_end': season_end,
           'home_teams': home_teams, 'guest_teams': guest_teams, 'users': users}
    return render(request, "season.html", context=ctx)


def login_view(request):
    return render(request, "login.html")
