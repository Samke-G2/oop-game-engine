"""
scenes.py
last modified: 24/10/2025

The scenes file will contain the scene class and all its objects, these will run each room (or situation) in the game
and be mapped for easy access.
"""
from textwrap import dedent

class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.inventory = ["knife", "torch"]

class Scene(object):
    
    def __init__(self):
        self.player = Player("Samkelwa")
    
    def enter(self):
        print("This class has not been configured, subclass it and try again")        
        
    
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
                You trip, fall, and hit your head on the chest.
                You die almost immediately.
            """)
        

class Fire_room(Scene):
    
    def __init__(self):
        super(Fire_room, self).__init__()
        self.dead = Dead()
    
    def enter(self):
        self.dead(dedent("""
            You enter a room with an angry fire demon in it.
            The demon spots you and burns you to a crisp.
        """)) 
        
                
class Death_room(Scene):
    
    def __init__(self):
        super(Death_room, self).__init__()
        self.dead = Dead()

    def enter(self):
        # pass
        print(dedent("""
            You enter a torch-lit room.
            There are two doors on either side of you.
            The door to your left is pitch black, with a bone handle.
            The door to your right is golden, with a diamond-encrusted handle.
            In front of you is a throne and on the throne sits a cloaked figure.
        """))
        print(dedent(f"""
            \"Hello, {self.player.name}.\", says the hooded man, \"I have been expecting you.\"
            \"I am Death, and I offer you a choice.\"
            \"One of these doors leads to your escape, and the other to your demise.\"
            \"The choice is yours...\"

            What do you do??
        """))
        
        choice = input("> ").lower()
        
        if "left" in choice:
            pass
            #call the next scene - Chest room
        elif "right" in choice:
            pass
            # call the next scene - Fire room
        else:
            self.dead("Death gets annoyed at your indecision and takes your soul.")
        

class Python_room(Scene):
    
    def __init__(self):
        super(Python_room, self).__init__()
        self.dead = Dead()
    
    def enter(self):
        print(dedent("""
            In this room there is a giant python in the process of strangling a man to death.
            There is also an open door to your right.
            The man notices you and croakes, \"I need your help, stranger. If you kill this snake for me, I can lead you to some hidden treasure.\"
                
            What do you do?
        """))
        
        choice = input("> ").lower()
        
        if ("help" in choice) or ("kill" in choice) or ("save" in choice) or ("cut" in choice) or ("stab" in choice) or ("snake" in choice) :
            self.dead("You miss your attack on the snake and it kills you.")
        elif "door" in choice:
            pass
            # chest_room(key)
        else:
            self.dead("The python kills the man and slithers over to do the same to you.")

class Spider_room(Scene):
    
    def __init__(self):
        super(Spider_room, self).__init__()
        self.dead = Dead()
        
    def enter(self):
        print(dedent("""
            You enter a room with a  giant spider in it.
            You notice a golden key on a ring around one of its spider's legs.
            The spider is preoccupied at the moment while you look around.

            To your left is a doorway, there is a bright light eminating from the room beyond.

            What do you do?
        """))
        
        choice = input("> ").lower()
        
        if ("spider" in choice) or ("kill" in choice) or ("cut" in choice) or ("stab" in choice) :
            print(dedent("""
                You manage to kill the spider before it notices you. 
                After it has died, you retrieve the key on its leg
            """))

            self.player.inventory.append("key")

            print("\nNow what do you do?")
            next = input("> ").lower()
            
            if ("back" in next) or ("return" in next):
                print(dedent("""
                    You return to the first room, faced with the same choices:
                    the door with the snake handle,
                    the door with the cobwebs,
                    and the one with the skull and crossbones.

                    Which do you choose now?
                """))

                sec_choice = input("> ").lower()

                if ("snake" in sec_choice):
                    pass
                    # python_room(key)
                elif ("cobwebs" in sec_choice):
                    pass
                    # spider_room(key)
                elif ("skull" in sec_choice):
                    pass
                    # death_room(key)
                else:
                    dead("You're paralysed by indecision until you die of starvation")

            elif "left" in next:
                pass
                # fire_room()
            else:
                self.dead("You fall on your knife and die.")
                
        elif ("left" in choice) or ("doorway" in choice):
            pass
            # fire_room()
        else:
            self.dead("The spider notices you and attacks, paralysing and killing you.")
        
        

class Start(Scene):
    
    def __init__(self):
        super(Start, self).__init__()
        self.dead = Dead()

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
        
        
class Finished(Scene):
    
    def __init__(self):
        super(Finished, self).__init__()
        
    def enter(self):
        print(f"Congratulations, {self.player.name}, You Won! ")
        print("Good Job!")
        
    return "finished"



# me = Player("Samkelwa")
test = Chest_room() 

test.enter()