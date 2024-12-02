from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import random
# Create your models here.

class Game (models.Model):
    player = models.CharField(
        max_length=1,
        choices=[
            ('X', 'X'),
            ('O', 'O'),
        ],
        default='X'
    )
    winner = models.CharField(
        max_length=10,
        default='pending',
    )
    round = models.IntegerField(
        default=1,
    )
    board = models.JSONField(
        default=list,
    )