#Learn Python 3 the Hard Way --> Ex 45: Build a game.
#--> Taking the game I built in ex43/44 and modifying it to add classes and objects and inheritances.
#We can import this whole sccript as a module

#Class Layout:
##############
#--> class Room() - main class
#--> class GameEngine() - keeps track of each room
#--> class FirstDoor() - The first room the user enters
#--> class SecondDoor() - The king's court
#--> class ThirdDoor() - The cave of dragons
#--> class FourthDoor() - The great hall
#--> class FifthDoor() - The garden of illusions
#--> class Treasure() - The treasure and game ending
#--> class Ending() - Displays losing and game over message if user loses
#--> class Win() - Displays winning message if user has won the game
#--> class StartGame() - This is the class that kicks off the game
#--> class GameFlow() - Has a dictioanry and manages movement from room to room along with the GameEngine() class.

#import modules/scripts here -->
from sys import exit

#This class has all the actions common to all the rooms
class Room(object):
    #Trying to create an introduction for each room in the Room class that is common to all the rooms/doors.
    intros = {
        1 : '\n====*====Welcome to the room of decisions..====*====\n',
        2 : '\n====*====Welcome to the kings court====*====\n',
        3 : '\n====*====Welcome to the cave of dragons====*====\n',
        4 : '\n====*====Welcome to the great hall====*====\n',
        5 : '\n====*====Welcome to the garden of illusions====*====\n',
        6 : '\n====*====Welcome to the Treasure vault, Choose wisely, Adventurer====*====\n'
    }
    # def enter(self):
    #     print("find all actions common to the rooms and put it here")
    
    # def __init__(self, intro):
    #     self.intro = intro

    #This fucntion is used to go through the dictionary and print out the dictonary key:value pair for each introduction.
    def next_intro(rooms):
        room_intro = Room.intros.get(rooms)
        return room_intro

#This class takes the info from the GameFlow class to kick off the game
#This keeps track of the game rooms and also kicks off the game
class GameEngine(object):

    def __init__(self, game_rooms):
        self.game_rooms = game_rooms
    #keeps track of the first room to begin the game and the last room to end it.
    def play(self):
        current_room = self.game_rooms.begin_game()
        final_room = self.game_rooms.next_door('win_game')

        while current_room != final_room:
            next_room_name = current_room.enter()
            current_room = self.game_rooms.next_door(next_room_name)

        current_room.enter()



#Creating a class defining the first room and start of the game:
class FirstDoor(Room):

    def enter(self):
        #This inherits from the Room class and calls the next_intro function in that class to display a welcome message.
        print(Room.next_intro(1))
        print("\nThere are two doors in this room, a red door and a blue door\n")
        print("Time to make a choice, red or blue :-)..??")
        door = input(">>> ")

        if door == "red":
            print("You have just fallen down the rabbit hole, wonder whats on the other side..hmmm.")
            return 'third_door'
        elif door == 'blue':
            return 'fifth_door'
        else:
            print("You have to choose between the red or blue door..Go back and start again.! :-| ")
            return 'first_door'


#Has a while loop then an if statement with nested if statements. 2 decision inputs from user
class SecondDoor(Room):

    def enter(self):
        #This inherits from the Room class and calls the next_intro function in that class to display a welcome message.
        print(Room.next_intro(2))
        print("You appear infront of the king..")
        print("The king says, 'I have a riddle for you'...Will you play? Yes or No?")
        decision = input(">>> ")

        while True:
            if "yes" in decision or "Yes" in decision:
                print("\nOk perfect..Here goes:")
                print(''' "I follow you all the time and copy your every move,
                but you can't touch me or catch me. What am I.?
                ''')
                decision = input(">>> ")

                if "shadow" in decision:
                    print("Awesome..Correct Answer..!! You can proceed...")
                    return 'fifth_door'
                else:
                    print("You failed the riddle...The king's guards throw you in the dungeon to starve to death..")
                    return 'the_end'
            else:
                print("Wrong answer...Start over.!!")
                return 'first_door'

#Whie loop takes input from user and depending on the decision sends the user to the next room
class ThirdDoor(Room):

    def enter(self):
        #This inherits from the Room class and calls the next_intro function in that class to display a welcome message.
        print(Room.next_intro(3))
        print("""You are in a giant cave...
        To your right is a dragon with a key around her neck
        and to your left is a giant eagle..Which one do you approach first.?""")

        while True:
            decision = input(">>> ")
            if "dragon" in decision:
                print("""The dragon actually belongs to a fairy, she picks you up on her back and flies off to meet her mistress...""")
                return 'treasure_room'
            elif "eagle" in decision:
                print("The eagle attacks you and pecks your eyeballs out..OUCH!!")
                print("you stumble around blind and bleed to death")
                return 'the_end'
            else:
                print("You have to pick between the dragon or the eagle to continue..")
                return 'third_door'

#User enters the fourth room and based on thier decison will move to the next stage or end the game.
class FourthDoor(Room):

    def enter(self):
        #This inherits from the Room class and calls the next_intro function in that class to display a welcome message.
        print(Room.next_intro(4))
        print("You are in a large hall full of food, there is a door at the other end..")
        print("Do you sit down and eat or do you ignore the food and walk through the door?")
        decision = input(">>> ")

        if "eat" in decision or "sit" in decision:
            print("""The food is posioned and left here for greedy people like you...
            You fall down dead after the first bite""")
            return 'the_end'
        elif "door" in decision or "walk" in decision or "ignore" in decision:
            print("Smart choice, the food was poisoned, You just made it to the next level")
            return 'third_door'
        else:
            ("You cannot decide so go back to the begining and start again...!")
            return 'first_door'

#class FifthDoor -- complete
################
#User is asked for an input to make a decision, if/else statements used to evaluate the decision and decide next step
class FifthDoor(Room):

    def enter(self):
        #This inherits from the Room class and calls the next_intro function in that class to display a welcome message.
        print(Room.next_intro(5))
        print("You just walked into a garden full of lions, do you run or stay?")
        decision = input(">>> ")

        if decision == "run":
            print("The hungry lions chase you down and eat you up...Ouch.!!")
            return 'the_end'
        elif decision == "stay":
            print("\nThe lions are guardians of the treasure trail and show you into a secret passage..\n")
            return 'third_door'
        else:
            print("That input is not allowed, please enter either run or stay.")
            return 'fifth_door'

#This class is the treasure room, user needs to make a decision
class Treasure(Room):

    def enter(self):
        print(Room.next_intro(6))
        print("\n The dragon brings you to the fairy's castle, and gives you the key around her neck..")
        print("You just unlocked the power of the magic fairy..")
        print("""She gives you 2 options:
        * 1. Take her hand and let her guide you through the garden or
        * 2. Take the magic wand she offers you and do it yourself.
        """)
        decision = input(">>> ")

        if "hand" in decision or "1" in decision:
            return 'win_game'
        elif "wand" in decision or "2" in decision:
            print("You do not have magic powers, The wand fails and the lions eat you up..")
            return 'the_end'
        else:
            print("Wrong choice, try again..")
            return 'treasure_room'

#This class displays the message when a player loses.
class Ending(Room):

    def enter(self):
        print("\nGame over, you lose...\n")
        print("\n==========THE END==========\n")
        exit(0)

#This class runs when a user wins the game by finding the treasure
class Win(Room):

    def enter(self):
        print('''\nThe magic fairy is the keeper of the treasure, 
        she guides you to the treasure chest and you unlock it with the dragons key..!\n''')
        print("CONGRATULATIONS, you have finished the game and won..!!!!")
        print("\n===========THE END==========\n")
        exit(0)

#this class will start the game:
#We create a list of numbers from 1 - 20 and user gets to pick from the list to begin the game.
class StartGame(object):

    def enter(self):
        options = []
        for i in range(0, 21):
            options.append(i)

        print("\nLet's play a treasue hunt game :-)\n")
        print("Pick a random number between 1 and 20")
        choice = int(input(">>> "))

        #first check if choice is between 1 - 20 and even
        if choice in options and choice % 2 == 0 and choice in range(1, 11):
            print("\nYou have chosen an even number between 1 & 10, proceed through door A.\n")
            return 'first_door'
        #check if choice is between 11 - 20 and even
        elif choice in options and choice % 2 == 0 and choice in range(11, 21):
            print("\nYou have chosen an even number greater than 10, proceed through door B.\n")
            return 'second_door'
        #check if choice is between 1 - 10 and odd
        elif choice in options and choice % 2 != 0 and choice in range(1, 11):
            print("\nYou have chosen an odd number less than 10, proceed through door C.\n")
            return 'third_door'
        #check if choice is between 11 - 20 and odd
        elif choice in options and choice % 2 != 0 and choice in range(11, 21) and choice != 13:
            print("\nYou have chosen an odd number greater than 10, proceed through door D\n")
            return 'fourth_door'
        #check if the number picked is 13
        elif choice in options and choice == 13:
            print("You just discovered the cheat code...")
            return 'win_game'
        #check if choice is in the list of numbers, if not start again
        elif choice not in options:
            print("""You must pick a number between 1 and 20. Try again: 
            ==========================================""")
            return 'start_game'
        else:
            print("Wrong choice...better luck next time :-( ")
            return 'the_end'
            exit(0)

#This class handles mapping and gameflow
class GameFlow(object):

    #Putting all the doors in our game in a dictionary as key:value pairs
    doors = {
        'start_game' : StartGame(),
        'first_door' : FirstDoor(),
        'second_door' : SecondDoor(),
        'third_door' : ThirdDoor(),
        'fourth_door' : FourthDoor(),
        'fifth_door' : FifthDoor(),
        'treasure_room' : Treasure(),
        'the_end' : Ending(),
        'win_game' : Win()
        
    }
    #This instantiates the object for this class.
    def __init__(self, starting):
        self.starting = starting
    #This gets the name of the next door from our doors dictionary & passes it to the door_val variable.
    def next_door(self, door_name):
        #this variable is used to get the diiferent door names
        door_val = GameFlow.doors.get(door_name)
        return door_val
    
    def begin_game(self):
        return self.next_door(self.starting)


# To begin the game:
######################
# #We have put this in a seperate file (ex45withImports.py) and imported the rest of the file as a module
# game_flow = GameFlow('start_game')
# my_game = GameEngine(game_flow)
# my_game.play()
