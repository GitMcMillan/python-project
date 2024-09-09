#!/usr/bin/env python3

class Enemy:
  def __init__(self, name, id=None ):
    self.id = id
    self.name = name
    self.hp = 5
    self.dmg = 5