#Using argv and input together:

#first import the argv module:
from sys import argv

#This means in addition to your script name which is an arguement, you have to give a username on the terminal as the 2nd arguement.
script, username = argv
#The prompt variable is set to whatever prompt we want that way we dont have to type it in alll the time.
prompt = ('>>>>')

print(f"Hi {username}, I am the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {username}")
likes = input(prompt)

print(f"Where do you live? {username}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Sounds like a cool place to live.
And you have a {computer} computer. Nice.
""")


