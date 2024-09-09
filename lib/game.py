#!/usr/bin/env python3
import random
import enemy
import player

class Game:
  def __init__(self, player, enemy):
    self.player = player
    self.enemy = enemy
    self.current_enemy = None

  def create_player(self):
    #create teh character
    while True:
      print("Create your character:")
      #player_name = input value
      player_name = input("What is your character name?")
      try:
        self.player = Player(player_name)
        #exit loop
        break
      except ValueError as e:
        print(e)
        continue

#create enemy (adjust player block)

  def create_enemy(self):
    #create teh enemy
    while True:
      print("Create enemy:")
      #enemy_name = input value
      enemy_name = input("What is the enemy name?")
      try:
        self.enemy = Enemy(enemy_name)
        #exit loop
        break
      except ValueError as e:
        print(e)
        continue
        #table creation. Save enemy to table
        self.enemy.create_table()
        self.enemy()

  #set up table


# def test():
#       print("working")


  