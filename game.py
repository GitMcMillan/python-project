#!/usr/bin/env python3

class Game:
  def __init__(self, player, enemy):
    self.player = player
    self.enemy = enemy
    self.current_enemy = None

  # def create_player(self):
  #   #create teh character
  #   while True:
  #     print("Create your character:")
  #     #player_name = input value
  #     player_name = input("What is your character name?")
  #     try:
  #       self.player = Player(player_name)
  #       #exit loop
  #       break
  #     except ValueError as e:
  #       print(e)
  #       continue


# def test():
#       print("working")


  