"""
scenes.py
last modified: 09/09/2025

The scenes file will contain the scene class and all its objects, these will run each room (or situation) in the game
and be mapped for easy access.
"""
from textwrap import dedent

class Player(object):
    
    def __init__(self, name):
        self.name = name

class Scene(object):
    
    def __init__(self):
        self.player = Player("Samkelwa")
    
    def enter(self):
        print("This class has not been configured, subclass it and try again")        
        
    
# Need to define the dead scene here at the start and create instance of that class before all others so the instance can be called within other classes flawlessly
class Dead(Scene):
    
    def __init__(self):
        super(Dead, self).__init__()
    
    def enter(self, reason):
        print(dedent(reason))
        print(dedent(f"""
            Good job, {self.player.name}!"
            "YOU LOSE!\n
        """))
    
class Chest_room(Scene):
    
    def __init__(self):
        super(Chest_room, self).__init__()
        self.dead = Dead()
    
    def enter(self):
        print(dedent("""
            You enter a room with a chest in the centre of it.
            The chest is locked and fixed to the floor.
            On the other side of the chest there is a door, opened a little bit.
            What do you do?
        """))
        
        choice = input("> ")

        if ("door" in choice) and (key == True):
            print("You look at the key in your hands, wondering what it does, before entering the door.")
            print("Through the door, you escape to the outside world.")
            print("You are alive and free, but without any treasure.")
            print(f"\nGood job, {self.player.name}, YOU LOSE!\n")
        elif ("door" in choice) and (key == False):
            print("Through the door, you escape to the outside world.")
            print("You are alive and free, but without any treasure.")
            print(f"\nGood job, {self.player.name}, YOU LOSE!\n")
        elif ("open" in choice) and (key == False):
            print("The chest is locked and you cannot open it without a key.")
            dead("You try to open it until you're exhausted, then you starve to death.")
        elif ("open" in choice) and (key == True):
            print("You use the key to open the chest.")
            print("Inside you find the most valuable diamond in the world.")
            print("After retrieving it, you enter through the open door and escape to the outside world.")
            print("You are alive, free, and unimaginably rich.")
            print(f"\nGood job, {self.player.name}, YOU WIN!\n")
        else:
            self.dead.enter("""
                You trip, fall, and hit your head on hte chest.
                You die almost immediately.
            """)
        

class Fire_room(Scene):
    
    def __init__(self):
        super(Fire_room, self).__init__()
    
    def enter(self):
        pass
        # call that "dead" scene here too
        
                
class Death_room(Scene):
    
    def __init__(self):
        super(Death_room, self).__init__()

    def enter(self):
        pass
        
        

class Python_room(Scene):
    
    def __init__(self):
        super(Fire_room, self).__init__()
    
    def enter(self, player):
        print(dedent("""
            In this room there is a giant python in the process of strangling a man to death.
            There is also an open door to your right.
            The man notices you and croakes, \"I need your help, stranger. If you kill this snake for me, I can lead you to some hidden treasure.\"
            \n    What do you do?
        """))
        
        choice = input("> ").lower()
    # This bit needs work on the function calls (will call an object in this iteration) will edit it after restructuring some of the earlier code.
        if ("help" in choice) or ("kill" in choice) or ("save" in choice) or ("cut" in choice) or ("stab" in choice) or ("snake" in choice) :
            pass
        #     dead(dedent("""
        # You miss your attack on the snake and it kills you.
        #     """))
        elif "door" in choice:
            pass
            # chest_room(key)
        else:
            pass
            # dead("    The python kills the man and slithers over to do the same to you.")

class Spider_room(Scene):
    
    def __init__(self):
        super(Fire_room, self).__init__()
    
    def enter(self, player):
        self.player = player
        

class Start(Scene):
    
    def __init__(self):
        super(Fire_room, self).__init__()

    def enter(self, player):
        print(dedent("""
            You are a treasure hunter.
            In your travels, you find an underground temple looking for lost wonders.

            After going down a long shaft, you end up in a blank room lit with torches all around.
            You are armed with a jungle knife, and a torch.

            There are three doors in the room:
            the one on your left has a handle that looks like the head of a snake,
            the one on your right has cobwebs on the corners of it,
            the one straight ahead has a skull and crossbones engraved on it.

            Which one do you go through?
        """))
        
        choice = input("> ").lower()

        # commented out sections need redoing under the new structure of things
        if ("left" in choice):
            pass
            # python_room(key)
        elif ("right" in choice):
            pass
            # spider_room(key)
        elif ("straight" in choice):
            pass
            # death_room(key)
        else:
            pass
            # dead("    You're paralysed by indecision until you die of starvation")
        



# me = Player("Samkelwa")
test = Chest_room() 

test.enter()