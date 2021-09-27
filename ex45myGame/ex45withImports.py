#This is a different version of the game where we are using the classes as modules and then importing them into this script.

#We import our orignal game with all the classes as a module in this script.
import ex45_myGame as mg

#Game code:
#We get the GameFlow class and methods from our import to use here.
game_flow = mg.GameFlow('start_game')
#We get the GameEngine class and its methods from our import to use here.
my_game = mg.GameEngine(game_flow)
#We call the play function on our game engine object to begin playing the game
my_game.play()