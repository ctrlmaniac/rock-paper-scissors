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
    def move(self):
        return "rock"


class TheCaothicOne(Player):
    def move(self):
        return random.choice(moves)


class TheMimic(Player):
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
        self.my_move_index = random.randint(0, 3)

    def move(self):
        if self.my_move_index == 0:
            self.my_move_index += 1
            return moves[0]
        elif self.my_move_index == 1:
            self.my_move_index += 2
            return moves[1]
        else:
            self.my_move_index = 0
            return moves[2]


class Human(Player):
    def move(self):
        choice = validate_input("Your move: rock, paper or scissors? ", moves)

        return choice


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player One: {move1} - Player Two: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if move1 != move2:
            if beats(move1, move2):
                self.p1_score += 1
            else:
                self.p2_score += 1

        print_pause(
            f"Score: Player One {self.p1_score}, "
            + f"Player Two {self.p2_score}\n",
            3,
        )

    def winner(self):
        winner = (
            "Player One" if self.p1_score > self.p2_score else "Player Two"
        )

        print(f"The winner is: {winner}!")

    def play_game(self):
        print_pause("\n===========\nGame start!\n===========\n")

        round = 0
        while True:
            round += 1
            print_pause(f"Round {round}:")
            self.play_round()

            if (self.p1_score == 3 or self.p2_score == 3) and (
                (self.p1_score > self.p2_score)
                or (self.p2_score > self.p1_score)
            ):
                break

        self.winner()


def computers_battle(players):
    player1 = players[random.randint(0, 3)]
    player2 = players[random.randint(0, 3)]

    game = Game(player1, player2)
    game.play_game()


def human_vs_computer(players):
    player1 = Human()
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

    print_pause("Welcome to Rock Paper Scissors!\n")
    print_pause("1. Do you want to play?")
    print_pause("2. Do you want to see other playing?")

    choice = validate_input("Type 1 o 2: ", ["1", "2"])

    if int(choice) == 1:
        human_vs_computer(players)
    else:
        computers_battle(players)
