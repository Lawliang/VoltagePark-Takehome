from django.test import TestCase, Client
from django.urls import reverse
from .models import Game
import json

class BasicEndpointTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create_game')
        self.fetch_url = lambda id: reverse('fetch_game', args=[id])
        self.move_url = lambda id: reverse('process_move', args=[id])

    def test_create_game_endpoint(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_fetch_game_endpoint(self):
        game = Game.objects.create(board=[""]*9)

        response = self.client.get(self.fetch_url(game.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], game.id)

    def test_make_move_endpoint(self):
        game = Game.objects.create(board=[""]*9, player="X", round=1)
        move_data = {
            "player": "X",
            "round": 1,
            "index": 0
        }
        # Test that the make move endpoint is accessible and returns a 200 status code
        response = self.client.post(self.move_url(game.id), data=json.dumps(move_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['board'][0], "X")
