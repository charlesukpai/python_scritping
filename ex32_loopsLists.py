#Using conditional statements to work on lists:

#my lists:
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots', 'mangoes']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Writing for loops that iterates through the lists:
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit is of type: {fruit}")

#Going through the list with mixed data types:
for i in change:
    print(f"I got {i}")

#Building a list, first we create an empty list:

elements = []

#range(0, 6) will take 0 - 5 inclusive and add it to our list.
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append() adds an item to the end of a list.
    elements.append(i)

#we can print out or new list using the for loop as well to iterate through the list:
for i in elements:
    print(f"Element was: {i}")
