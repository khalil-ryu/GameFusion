# mainapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Game

def home(request):
    return render(request, 'mainapp/home.html')

def game(request):
    return render(request, 'mainapp/game.html')

@login_required
def profile(request):
    return render(request, 'mainapp/profile.html')

def game(request):
    links = [
        "https://play.unity.com/mg/other/delivery-driver-8",
        "https://play.unity.com/mg/other/snow-boarder-1",
        "https://play.unity.com/mg/other/my-gamedev-tv-tilevania-project",
        "https://play.unity.com/mg/other/rock-paper-scissors-4",
        "https://play.unity.com/mg/other/uy-studios-tic-tac-toe-basic-ai-version",
    ]
    loop_range = range(5)

    games = Game.objects.all()
    return render(request, 'mainapp/game.html', {'games': games, 'links':links, 'i': 0})