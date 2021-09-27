#Using while loops.
#A while loop will keep executing for as long as a Boolean Expression/condition is True until it becomes False.
#NOTES:
#Review your whille loop to make sure that the condition equates to False at some point to break the loop or it will run forever.
#When in doubt, print out your test variable at the top and bottom of the loop to see what it is doing.
#for loops may be a better option than while loops in most cases.

#Main Exercise Code:
####################
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is {i}")

print("The numbers: ")
for num in numbers:
    print(num)




# #Study Drill 1:
# ###############
# #defining a function to use for our looping:
# #The rng gives us the max upper limit for the list and incr gives us the amount by which we increment i
def create_list(rng, incr):
    i = 0
    #defining an empty list
    x = []
    #this while loop will break once i becomes greater than rng value.
    while i < rng:
        print(f"At the top i is {i}")
        x.append(i)
        print("Enter a value between 0 and 10 to increment i by: ")
        i = i + incr
        print("Numbers now: ", x)
        print(f"At the bottom is {i}")

    print("The numbers: ")

    for num in x:
        print(num)

#Creating new emptys list my_list by calling our create_list() function and passing it arguements for the range and increment:
print("\nUsing 10 for our arguement value and an increment of 2:\n")
create_list(10, 2)

print("\nUsing 20 for our argument value and an increment of 4:\n")
create_list(20, 4)


#Study Drill 2:
###############
#Using a for loop instead of the while loop.
#The for loop and range() eliminates the need for the incrementor as we can just tell range what the increment should be.

def make_list(x, y):
    nu_list = []
    #Here we specify for the range() that we want to start at 0. We also specify the end of the range (x) and the increment (y).
    for i in range(0, x, y):
        nu_list.append(i)

    print(nu_list)

print("\nHere's trying some argeuments:\n")
print("Our list becomes: ")
make_list(100, 5)

