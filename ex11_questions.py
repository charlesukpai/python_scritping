#Switiching over to the newer edition of the book which uses python 3.6
#Ex is asking questions.

print("How old are you?", end=' ')
#The e='' at the end of the print statement tells the print not to end the line with a newline character and to go to the next line.
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you are {age} old, {height} tall and {weight} heavy.")
