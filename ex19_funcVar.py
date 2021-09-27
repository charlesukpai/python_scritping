#Using functions and variables together:

#writing a fucntion
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} boxes of cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man thats enought for a party!")
    print("Get a blanket. \n")

#calling the function:
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#assiging variables:
print("Or we can use variables from our script:")
#using int() converts the value you give to input to an integer:
amount_of_cheese = int(input("Enter amount of cheese: "))
amount_of_crackers = int(input("Enter amount of crackers: "))

#calling the variables with our function:
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
