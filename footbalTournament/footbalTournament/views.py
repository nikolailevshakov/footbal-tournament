from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath('..'))
from my_app.forms import RegisterForm
from . import views
from django.views.generic import TemplateView, CreateView, ListView
from my_app.models import User


# class based view
class HomeView(TemplateView):
    template_name = 'index.html'


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


# model based classView
class UserCreateView(CreateView):
    model = User
    fields = ["name", "email", "password"]
    success_url = 'account/'

# to list objects from db
# class UserListView(ListView):
#     model = User
#     context_object_name = 'user_list'

# def login_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse(views.account_view))
#     else:
#         form = RegisterForm()
#     return render(request, "login.html", context={'form':form})


def account_view(request):
    return render(request, "account.html")
