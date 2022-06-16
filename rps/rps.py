#!/usr/bin/env python3

import random
import time

moves = ["rock", "paper", "scissors"]


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


def print_pause(string, sleep=1):
    print(string)
    time.sleep(sleep)


def validate_input(prompt, options):
    while True:
        option = input(prompt).lower()

        if option in options:
            return option

        print("Sorry, I didn't understand! Try Again!")


class Player:
    def __init__(self):
        self.my_moves = []
        self.their_moves = []
        self.name = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class TheRock(Player):
    def __init__(self):
        super().__init__()
        self.name = "The Rock"

    def move(self):
        return "rock"


class TheCaothicOne(Player):
    def __init__(self):
        super().__init__()
        self.name = "The Chaotic One"

    def move(self):
        return random.choice(moves)


class TheMimic(Player):
    def __init__(self):
        super().__init__()
        self.name = "The Mimic"

    def learn(self, my_move, their_move):
        self.my_moves.append(my_move)
        self.their_moves.append(their_move)

    def move(self):
        try:
            return self.their_moves[-1]
        except IndexError:
            return random.choice(moves)


class TheNonStrategicOne(Player):
    def __init__(self):
        super().__init__()
        self.my_move_index = 0
        self.name = "The Non-Strategic One"

    def move(self):
        if self.my_move_index == 2:
            self._my_move_index = 0
            return moves[self.my_move_index]
        else:
            self.my_move_index += 1
            return moves[self.my_move_index]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"{self.p1.name}: {move1}  {self.p2.name}: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Game start!\n")

        for round in range(3):
            print_pause(f"Round {round}:")
            self.play_round()

        print_pause("Game over!")


def computers_battle(players):
    player1 = players[random.randint(0, 3)]
    player2 = players[random.randint(0, 3)]

    game = Game(player1, player2)
    game.play_game()


if __name__ == "__main__":
    players = [
        TheRock(),
        TheMimic(),
        TheNonStrategicOne(),
        TheCaothicOne(),
    ]

    print_pause("Welcome to Rock Paper Scissors!")
    print_pause("1. Do you want to play?")
    print_pause("2. Do you want to see other playing?")

    choice = validate_input("Type 1 o 2: ", ["1", "2"])

    if int(choice) == 1:
        pass
    else:
        computers_battle(players)
