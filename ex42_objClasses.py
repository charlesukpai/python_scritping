#Fish  is a class
#Salmon is a class because it is a fish but has salmon like attributes
#mary a salmon is an object as it is an instance of salmon as well as being a fish
#is-a = Used when you talk about relationships between a class and an object
#has-a = Used when talking about objects and classes that reference each other
#Remember, is-a is the relationship between fish and salmon, while has-a is the relationship between
#salmon and gills.
#Formally, an object is a collection of data and associated behaviors.
#Object-oriented programming means writing code directed toward modeling objects
#An object is a collection of data with associated behaviors. Class = a kind of object
#Note:
######
#Classes describe related objects - Classes are blueprints for creating objects.
#Objects have attributes and behaviors of the class they belong to.
#Instances of 2 classes related by association. E.g Apples go in a Barrel. Both apple and barrel are classes and are associated.
#Relationshps between different classes of objects described using Unified Modeling language (UML).
# Data represents the individual characteristics of a certain object; its current state.



#Animal is-a object
class Animal(object):
    pass

#dog is a class
class Dog(Animal):

    def __init__(self, name):
        #object
        self.name = name

#Cat is a class
class Cat(Animal):

    def __init__(self, name):
        #object
        self.name = name

#person is an object
class Person(object):
    def __init__(self, name):
        #object
        self.name = name
        #person has a pet
        self.pet = name

# Employee is a class
class Employee(Person):
    def __init__(self, salary):
    #strange magic
        super(Employee, self).__init__(salary)
        #salary is an object
        self.salary = salary

 