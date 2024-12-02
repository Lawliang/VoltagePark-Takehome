# django api
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# direct imports
from .models import Game
from .cache import save_cached_game, fetch_cached_game
from .logic import check_winner
# etc. imports
import json
import random

# Create your views here.
@csrf_exempt
def CreateView(request):
    # creates a new game in database
    try: 
        game = Game.objects.create(board=[""]*9)
        game_dict = model_to_dict(game)
        return JsonResponse(game_dict, status=200)
    except Game.DoesNotExist:
        return JsonResponse({"error": "Failed to create a game."}, status=404)

@csrf_exempt
def FetchView(request, id):
    # fetches the game state from last session
    try:
        game = Game.objects.get(id=id)
        game_dict = model_to_dict(game)
        return JsonResponse(game_dict, status=200)
    except Game.DoesNotExist:
        return JsonResponse({"error": "Game not found."}, status=404)

@csrf_exempt
@require_POST
def MoveView(request, id):
    move = json.loads(request.body)
    required_fields = ['player', 'round', 'index']
    if not all(field in move for field in required_fields):
        return JsonResponse({"error": "Missing required fields."}, status=400)

    game = fetch_cached_game(id)
    if game["winner"] != "pending":
        return JsonResponse({**game, "error": "Game is completed."}, status=400)
    if game["player"] != move["player"]:
        return JsonResponse({**game, "error": "Incorrect player."}, status=400)
    if game["board"][move["index"]] != "":
        return JsonResponse({**game, "error": "Invalid move placement."}, status=400)
    if move["round"] != game["round"]:
        return JsonResponse({**game, "error": "Invalid round."}, status=400)
    # update game
    game["board"][move["index"]] = move["player"]
    game["player"] = "O" if game["player"] == "X" else "X"
    game["round"] += 1
    winner = check_winner(game["board"])
    if winner:
        game["winner"] = winner
    elif game["round"] > 9:
        game["winner"] = "Tie"
    # save game to cache & db
    save_cached_game(id, game)
    return JsonResponse(game)