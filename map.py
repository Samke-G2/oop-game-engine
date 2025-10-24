"""
map.py
last modified: 24/10/2025

The map file will collect all the scenes of the game and map them out into a dictionary for easy access.
"""
import scenes.py

class Map(object):
    
    scenes = {
        "start_room": scenes.Start(),
        "chest_room": scenes.Chest_room(),
        "fire_room": scenes.Fire_room(),
        "death_room": scenes.Death_room(),
        "python_room": scenes.Python_room(),
        "spider_room": scenes.Spider_room(),
        "finished": scenes.Finished
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
    
    
    
    