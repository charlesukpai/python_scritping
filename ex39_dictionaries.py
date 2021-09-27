#Dictionary data structure
#unlike lists you are not restrictued to indexing dictioanries with numbers alone:
#Mapping and associations is the main concept in a dictionary. Maps items to keys in the format {Key:Value}.
#NOTES:
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


#Creating a mapping of US states to their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Ohio': 'OH',
}

#Creating a mapping of US states and cities
cities = {
    'CA': 'Los Angeles',
    'FL': 'Miami',
    'OH': 'Cincinnati',
    'NY': 'Brooklyn',
    'MI': 'Detroit'
}

#Add more cities:
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

#print out some cities:
print('-' * 20)

print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#printing some states:
print('-' * 20)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#Lets try this using states then cities dict:
print('-' * 20)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#Let's print every state abbreviation:
print('-' * 20)
#The for loop simply says for each key, value get the items or key:value pair.
#state and abbrev are variables initiated when the loop runs used to hold the values and print them.
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

#Doing both state and city together:
print('-' * 30)
#For loop runs through the dictioanry and gets each key, value pair and assigns them to the variables state & abbrev
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and city has {cities[abbrev]}")

print('-' * 30)
#try to get a state not there and display a message if state is not in the options:
state = states.get('Texas')

if not state:
    print("Sorry no Texas in the options")

#Get a city with a default value:
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

print(f"The states dictionary is {len(states)} long")
print(f"The cities dictioanry is {len(cities)} long")