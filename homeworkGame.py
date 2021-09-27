#LEARN PYTHON THE HARD WAY:
#EXERCISE 36 HOMEWORK:
#Building a game from scratch.

from sys import exit

#guess a number, if number is between 1 and 20 open a door, if not do soemthing else.
#number gets you a door, inside the door do something to proceed or get killed
#guessing 13 wins the game
#if not, get to the room with the treasure.

#first function:
################
#Makes you choose between 2 doors red/blue. takes string input from user.
#then calls other functions depending on the user's decision/choice.
def first_door():
    print("\nWelcome to the wonzy room ;-)\n")
    print("\nThere are two doors in this room, a red door and a blue door\n")
    print("Time to make a choice, red or blue :-)..??")
    door  = input(">>> ")

    if door == "red":
        print("You have just fallen down the rabbit hole, wonder whats on the other side..hmmm.")
        third_door()
    elif door == "blue":
        fifth_door()
    else:
        print("You have to choose between the red or blue door..Go back and start again.! :-| ")
        start_game()

#second function:
#################
#Has a while loop then an if statement with nested if statements. 2 decision inputs from user
def second_door():
    print("You appear infront of the king..")
    print("The king says, 'I have a riddle for you'...Will you play? Yes or No?")
    decision = input(">>> ")

    #test to see how this runs: Ran ok.
    while True:
        if "yes" in decision or "Yes" in decision:
            print("\nOk perfect..Here goes:")
            print(''' "I follow you all the time and copy your every move,
            but you can't touch me or catch me. What am I.?
            ''')
            decision = input(">>> ")

            if "shadow" in decision:
                print("Awesome..Correct answer..! You can proceed..")
                fifth_door()
            else:
                print("You failed the riddle...The king's guards throw you in the dungeon to starve to death..")
                the_end()
        else:
            print("Wrong Answer...Start over!")
            start_game()

#third function:
################
#Has a while loop that evaluates the users input. 2 choices between dragon and eagle
#Calls 2 other functions depending on the user's response
def third_door():
    print("""You are in a giant cave...
    To your right is a dragon with a key around her neck
    and to your left is a giant eagle..Which one do you approach first.?""")
    
    while True:
        decision = input(">>> ")
        if "dragon" in decision:
            print("""The dragon actually belongs to a fairy, 
            she picks you up on her back and flies off to meet her mistress...""")
            treasure()
        elif "eagle" in decision:
            print("The eagle attacks you and pecks your eyeballs out..OUCH!!")
            print("you stumble around blind and bleed to death")
            the_end()
        else:
            print("You have to pick between the dragon or the eagle to continue..")

#fourth function:
###################
#if statement evaualtes user input and calls 3 other functions depending on the user's decision.
def fourth_door():
    print("You are in a large hall full of food, there is a door at the other end..")
    print("Do you sit down and eat or do you ignore the food and walk through the door?")
    decision = input(">>> ")

    if "eat" in decision or "sit" in decision:
        print("""The food is posioned and left here for greedy people like you...
        You fall down dead after the first bite""")
        the_end()
    elif "door" in decision or "ignore" in decision or "walk" in decision:
        print("Smart choice, the food was poisoned, You just made it to the next level")
        third_door()
    else:
        ("You cannot decide so go back to the begining and start again...!")
        start_game()

#fifth function:
################
#Function asks the user for a decision then calls 2 other functions based on the choice they make.
def fifth_door():
    print("You just walked into a garden full of lions, do you run or stay?")
    decision = input(">>> ")

    if decision == "run":
        print("The hungry lions chase you down and eat you up...Ouch.!!")
        the_end()
        exit(0)
    elif decision == "stay":
        third_door()
    else:
        print("That input is not allowed, please enter either run or stay.")

#sixth function:
################
#Function asks the user for a decision then calls 2 other functions based on the choice they make.
def treasure():
    print("\n The dragon brings you to the fairy's castle, and gives you the key around her neck..")
    print("You just unlocked the power of the magic fairy..")
    print("""She gives you 2 options:
    * 1. Take her hand and let her guide you through the garden or
    * 2. Take the magic wand she offers you and do it yourself.
    """)
    decision = input(">>> ")

    if "hand" in decision or "1" in decision:
        print("The fairy is the keeper of the treasue and guides you to your riches..!!!")
        print("CONGRATULATIONS, You found the treasure, you have finsihed the game and won..!!!!")
        print("\n===========THE END==========\n")
        exit(0)
    elif "wand" in decision or "2" in decision:
        print("You do not have magic powers, The wand fails and the lions eat you up..")
        the_end()
        exit(0)
    else:
        print("Wrong choice, you are transported back to the beginining...Start over.!")
        start_game()

#seventh function:
##################
#This function is used to end the game when a user loses and print out the end game message
def the_end():
    print("\nGame over, you lose...\n")
    print("=========THE END=========")
    #Had to add an exit statement here so when this function is called it also exits the game
    #Had to do this as third_door() keept looping.
    exit(0)

#eight function:
################
#This is the main function that starts the game. It first initiates an empty string, fills it with integers
#Then the user has to pick from within a range of numbers to begin playing the game.
#Each number picked even or odd has to be between 1 - 20 and a function is called depending on the num.
def start_game():
    options = []
    for i in range(0, 21):
        options.append(i)
    # print(options)

    print("\nLet's play a treasue hunt game :-)\n")
    print("Pick a random number between 1 and 20")
    choice = int(input(">>> "))
    
    #if choice is between 1 - 10 and even
    if choice in options and choice % 2 == 0 and choice in range(1, 11):
        print("\nYou have chosen an even number less than 10, proceed through door A.\n")
        first_door()
    #if choice is between 11 - 20 and even
    elif choice in options and choice % 2 == 0 and choice in range(11, 21):
        print("\nYou have chosen an even number greater than 10, proceed through door B.\n")
        second_door()
    #if choice is between 1 - 10 and odd
    elif choice in options and choice % 2 != 0 and choice in range(1, 11):
        print("\nYou have chosen an odd number less than 10, proceed through door C.\n")
        third_door()
     #if choice is between 11 - 20 and odd
    elif choice in options and choice % 2 != 0 and choice in range(11, 21) and choice != 13:
        print("\nYou have chosen an odd number greater than 10, proceed through door D\n")
        fourth_door()
    elif choice == 0 or choice > 20:
        print("""You must pick a number between 1 and 20. Try again: 
         ==========================================""")
        start_game()
    #if choice is 13 then end game print congratulations and exit.
    elif choice in options and choice == 13:
        print("CONGRATULATIONS, You guessed the magic number right and have won the game..!!!!!! ;-) ")
        print("=========THE END=========")
        exit(0)
    else:
        print("Wrong choice...better luck next time :-( ")
        the_end()
        exit(0)
      
#We call the start_game() funtion here to begin the game.    
start_game()