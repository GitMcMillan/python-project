#!/usr/bin/env python3

#thingds you need
#name, id, hp, inventory (list?), damage? or weapon? victory condition in player instance?

class Player:
  def __init__(self, name, id=None):
    self.name = name
    self.id = id
    self.inventory = []
    self.dmg = 1
    self.win = False
