from django.core.cache import cache
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Game

ttl = 300 # 5 minutes

def save_cached_game(id, game):
    cache.set(f'game_{id}', game, ttl)
    # potential refactor: push this to a background task via celery to act in async
    print(game)
    Game.objects.filter(id=id).update(
         board=game["board"],
         player=game["player"],
         round=game["round"],
         winner=game["winner"],
    )
    return

def fetch_cached_game(id):
    game = cache.get(f'game_{id}')
    if not game:
        try:
            game = Game.objects.get(id=id)
            game_dict = model_to_dict(game)
            print('Fetching game and setting in cache!')
        except Game.DoesNotExist:
                return JsonResponse({"error": "Game not found (turn)."}, status=404)
        cache.set(f'game_{id}', game_dict, ttl) # save game in cache for future requests
        return game_dict
    return game