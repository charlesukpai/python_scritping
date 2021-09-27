
from sys import exit

#Function 1:
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number..")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win!!!")
        #Passing exit(0) to the system means a good exit with no errors.
        exit(0)
    else:
        dead("You greedy bastard.!!")

#Function 2:
def bear_room():
    print("There is a bear in here.")
    print("The bear has a bunch of honey")
    print("The fat bear is infront of another door.")
    print("How are you going to move the bear.?")
    bear_moved = False

    print("""Please choose one of the following options:
    *take honey
    *taunt bear
    *open door
    """)
    while True:
        choice = input(">> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

#Function 3:
def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head.?")

    choice = input(">> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty.!")
    else:
        cthulhu_room()

#Function 4: - The why variable takes whatever string you defined when you called dead() inside the other functions.
def dead(why):
    print(why, "Good job..!")
    exit(0)

#Function 5: - This is the first function that runs.
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take.?")

    choice = input(">> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
