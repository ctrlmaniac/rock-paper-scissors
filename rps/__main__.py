from __future__ import absolute_import

from rps import Game, TheRock, TheMimic, TheNonStrategicOne, TheCaothicOne
import random

players = [
    TheRock(),
    TheMimic(),
    TheNonStrategicOne(),
    TheCaothicOne(),
]

player1 = players[random.randint(0, 3)]
player2 = players[random.randint(0, 3)]

game = Game(player1, player2)
game.play_game()
