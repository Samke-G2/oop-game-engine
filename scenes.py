"""
scenes.py
last modified: 09/09/2025

The scenes file will contain the scene class and all its objects, these will run each room (or situation) in the game
and be mapped for easy access.
"""
class Scene(object):
    
    def enter(self, player):
        self.player = player
        pass
    
    
