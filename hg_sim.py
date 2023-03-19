# This is a better Hunger Games Simulator
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.health = "healthy"
    def __str__(self):
        return self.name

class Alliance:
    def __init__(self, player_subset):
        self.player_subset = player_subset

events = {"run": "ran away",
          "hunt tributes": "hunted for tributes",
          "shelter": "found shelter",
          "kill": "killed"}

def make_players(n=12):
    players = []
    for i in range(n+1):
        temp_name = input("Next Player's Name:  ")
        players.append(Player(temp_name))
    print("Here are all the players:")
    print([str(player) for player in players])
    answer = input("Look good? (y/n?):  ")
    if answer in ["y", "Y", " y", " Y"]:
        return players
    else:
        print("Try again:")
        return make_players(n)

def new_day(players, day=1):
    if len(players) == 1:
        print("Congratulations to ", players[0])
        return None
    else:
        if day==1:
            print("DAY 1")
            print("First day: Blood Bath Day")
        for p in players:
            event = random.choice(list(events.keys()))
            if event == "kill":
                victim = random.choice(players)
                players.remove(victim)
                if victim == p:
                    print(p, "committed suicicide")
                else:
                    print(p, events[event], victim)
            else:
                print(p, " ", events[event])
        print("DAY ", str(day+1))
        proceed = input("Proceed to next day?  ")
        if proceed == "y":
            return(new_day(players, day=day+1))
        else:
            print("goodbye")
            return None

def start_game(n=12):
    players = make_players(n)
    new_day(players)
    return None

n = int(input("Number of players:  "))
start_game(n)
