#Using Else and If statements.
#If multiple elif blocks are true, python starts from the top and only runs the first one true.

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not takes the cars.")
else:
    print("We cant decide.")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cant decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


