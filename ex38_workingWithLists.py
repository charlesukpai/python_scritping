#Working with lists:
#One of the most commonly used data structures:
#To find a specific item on a list, you start from the begining and go in order

#When to use the list data structure:
#1. When you need to maintain order. Lists will not sort or order for you so you have to specify.
#2. If you need to access data randomly using a number/index starting at zero.
#3. If you need to linearly go through the data first to last. E.g using for loops.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list, lets fix that:")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

