#!/usr/bin/env python3
import time
import random
import getpass
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


def getrounds():
    while True:
        rounds = input("How many rounds of game ? (Enter a number) : ")
        if rounds.isdigit():
            rounds = int(rounds)
            return rounds


def slow(sec):  # A time delay
    time.sleep(sec)


# This counts the score, increasing the star<list> by 1 more of its element ;
# ...Imports score from beats(); Imports move1() and move2() which is a list. ;
def countscore(score, star, move1, move2):
    if score == "Win":
        print(f"***{move1[0]} Player 1 wins!***")
        star.append("1")
        return star
    elif score == "Lose":
        print(f"***{move2[0]} Player 2 wins!***")
        star.append("2")
        return star
    elif score == "Draw":
        print(f"***This is tie.***")
        star.append("3")
        return star


class Player:  # Making a player, there are 4 moves.
    def setting1(self):  # Ask if the player is a human or android.
        identity1 = input("Player 1 : Are you a Human or Android ? : ")
        while identity1 != "Human" and identity1 != "Android":
            identity1 = input(f"Player 1 , Please choose either "
                              "'Human' or 'Android' : ")
        slow(2)
        return identity1

    def setting2(self):
        identity2 = input("Player 2 : Are you a Human or Android ? : ")
        while identity2 != "Human" and identity2 != "Android":
            identity2 = input(f"Player 2 , Please choose either "
                              "'Human' or 'Android' : ")
        return identity2

    def get_name(self):  # Get the whenever a human player is added.
        name = input("What is your name ? ")
        return name


# The computer cycle the order of "Rock","Paper", and "Scissors".
class cycle(Player):
    def cycle_move(self, numberofcycle):
        num1 = numberofcycle.count("cycle1")
        num2 = numberofcycle.count("cycle2")
        if num1 % 2 == 1:
            move = "Rock"
            if num1 % 3 == 0:
                move = "Scissors"
        elif num1 % 2 == 0:
            move = "Paper"
            if num1 % 3 == 0:
                move = "Scissors"
        if num2 % 2 == 1:
            move = "Rock"
            if num2 % 3 == 0:
                move = "Scissors"
        elif num2 % 2 == 0:
            move = "Paper"
            if num2 % 3 == 0:
                move = "Scissors"
        name = "Computer"
        print("Cycling")
        return [name, move]


# The computer learns the previous human's move.
class learn1(Player):
    def learn(self, their_move, round):
        move2 = their_move[round-1]
        print("Swagging move2")
        return ["Computer", move2]


class human(Player):
    def human_move(self):  # Manually as the human player what move he chooses.
        game = []
        name = self.get_name()
        game.append(name)
        print("Your move will not be shown. ")
        slow(2)
        choice = getpass.getpass("Choose one (Rock, Scissors or Paper) : ")
        while choice != "Rock" and choice != "Paper" and choice != "Scissors":
            choice = getpass.getpass(f"Please type either "
                                     "'Rock', 'Scissors' or 'Paper'"
                                     " as it is shown: ")
        game.append(choice)
        return game


class rock(Player):
    def rock_move(self):  # The computer only knows how to play "Rock".
        return ["Computer", "Rock"]


class randomc(Player):
    def random_move(self):  # The computer chooses random move.
        move = ['Rock', 'Paper', 'Scissors']
        move = random.choice(move)
        name = "Computer"
        return [name, move]


def findll(lis):  # Find the class <list> in a list.
    i = 0
    for item in lis:
        if type(item) == list:
            i += 1
        else:
            i = 0
    return i


def beats(one, two):  # To decive who wins the round.
    if ((one == 'Rock' and two == 'Scissors') or
            (one == 'Scissors' and two == 'Paper') or
            (one == 'Paper' and two == 'Rock')):
        return "Win"
    else:
        if ((one == 'Rock' and two == 'Rock') or
                (one == 'Scissors' and two == 'Scissors') or
                (one == 'Paper' and two == 'Paper')):
            return "Draw"
        else:
            return "Lose"


# 4 Scenarios: 1.(Human vs Human) ; 2.(Human vs Android) ;
# 3.(Android vs Human) ; 4.(Android vs Android).
class Game:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

# The star input is a list that collects the
# information about the specific round.
    def play_round(self, star):
        # Ask if the player is a Human or Computer.
        type1 = self.player1.setting1()
        type2 = self.player2.setting2()
        if type1 == "Human" and type2 == "Human":  # Scenario 1
            print("Player 1's information")
            move1 = human.human_move(self.player1)
            print("Player 2's information")
            move2 = human.human_move(self.player2)
            score = beats(move1[1], move2[1])
            print(f"{move1[0]} plays {move1[1]}, "
                  f"and {move2[0]} plays {move2[1]}")
            countscore(score, star, move1, move2)
            return star
        elif type1 == "Human" and type2 == "Android":  # Scenario 2
            print("Player 1's information")
            move1 = human.human_move(self.player1)
            round = star.count("1")+star.count("2")+star.count("3")
            if round > 0:
                star[0].append(move1[1])
            else:
                star.append([move1[1]])
            strategy = ["1", "2", "3", "4"]
            strategy2 = random.choice(strategy)
            if strategy2 == "1" or strategy2 == "4":
                if strategy2 == "4" and round > 0:
                    move2 = learn1.learn(self.player2,
                                         star[findll(star)], round)
                else:
                    move2 = rock.rock_move(self.player2)
            elif strategy2 == "2" or strategy2 == "4":
                if strategy2 == "4" and round > 0:
                    move2 = learn1.learn(self.player2,
                                         star[findll(star)], round)
                else:
                    move2 = randomc.random_move(self.player2)
            elif strategy2 == "3" or strategy2 == "4":
                if strategy2 == "4" and round > 0:
                    move2 = learn1.learn(self.player2,
                                         star[findll(star)], round)
                else:
                    star.append("cycle2")
                    move2 = cycle.cycle_move(self.player2, star)
            score = beats(move1[1], move2[1])
            print(f"{move1[0]} plays {move1[1]} ,"
                  f"and {move2[0]} plays {move2[1]}")
            countscore(score, star, move1, move2)
            return star
        elif type2 == "Human" and type1 == "Android":  # Scenario 4
            print("Player 2's information")
            move2 = human.human_move(self.player2)
            round = star.count("1")+star.count("2")+star.count("3")
            strategy = ["1", "2", "3", "4"]
            strategy1 = random.choice(strategy)
            if strategy1 == "1" or strategy1 == "4":
                if strategy1 == "4" and round > 0:
                    move1 = learn1.learn(self.player1,
                                         star[findll(star)], round)
                else:
                    move1 = rock.rock_move(self.player1)
            elif strategy1 == "2" or strategy1 == "4":
                if strategy1 == "4" and round > 0:
                    move1 = learn1.learn(self.player1,
                                         star[findll(star)], round)
                else:
                    move1 = randomc.random_move(self.player1)
            elif strategy1 == "3" or strategy1 == "4":
                if strategy1 == "4" and round > 0:
                    move1 = learn1.learn(self.player1,
                                         star[findll(star)], round)
                else:
                    star.append("cycle1")
                    move1 = cycle.cycle_move(self.player1, star)
            score = beats(move1[1], move2[1])
            print(f"{move1[0]} plays {move1[1]} ,"
                  f"and {move2[0]} plays {move2[1]}")
            countscore(score, star, move1, move2)
            return star
        elif type1 == "Android" and type2 == "Android":  # Scenario 4
            strategy = ["1", "2", "3"]
            strategy1 = random.choice(strategy)
            strategy2 = random.choice(strategy)
            if strategy1 == "1":
                move1 = rock.rock_move(self.player1)
            elif strategy1 == "2":
                move1 = randomc.random_move(self.player1)
            elif strategy1 == "3":
                star.append("cycle1")
            if strategy2 == "1":
                move2 = rock.rock_move(self.player2)
            elif strategy2 == "2":
                move2 = randomc.random_move(self.player2)
            elif strategy2 == "3":
                star.append("cycle2")
            if strategy1 == "3" and strategy2 == "3":
                move1 = cycle.cycle_move(self.player1, star)
                move2 = cycle.cycle_move(self.player2, star)
            elif strategy1 == "3":
                move1 = cycle.cycle_move(self.player1, star)
            elif strategy2 == "3":
                move2 = cycle.cycle_move(self.player2, star)
            score = beats(move1[1], move2[1])
            print(f"{move1[0]} plays {move1[1]} ,"
                  f"and {move2[0]} plays {move2[1]}")
            countscore(score, star, move1, move2)
            return star

    def play_game(self):
        print("Game start!\n")
        slow(0.5)
        rounds = getrounds()
        slow(0.5)
        print("Here we start!!\n")
        score = []
        for round in range(rounds):
            slow(0.5)
            print(f"Round {round}:")
            score = self.play_round(score)
            print("\n")
        player1 = score.count("1")
        player2 = score.count("2")
        playerdraw = score.count("3")
        if player1 > player2 and player1 > playerdraw:
            print("Player 1 wins the game.\n")
        elif player2 > player1 and player2 > playerdraw:
            print("Player 2 wins the game.\n")
        elif player1 == player2:
            print("This game is tie!\n")
        print("Game is over!")


if __name__ == '__main__':
    game = Game(Player(), Player())  # p1= Player(); p2=Player()
    game.play_game()
