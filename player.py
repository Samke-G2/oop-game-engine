"""
player.py
last modified: 09/09/2025

Here we will store the player class which will contain all the player's info and
the inventory where everything the player picks up will be stored.
"""

class Player(object):
    
    def __init__(name):
        self.name = name
        self.health = 500 
        self.inventory = [knife, torch]
 