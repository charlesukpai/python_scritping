#Using classes in python
#This is Object Oriented programming
#Classes are like modules
#When you call or create a class, you instantiate that class and an object of that class is created
#the __init__() function is used to initialized the new object created when your class is instansiated
#calling a class uses the class to build a copy(object) with same attributes as the class
#Note:-
#Inside the functions in a class, self is a variable for the instance/object being accessed.

#creating a class:
class Song(object):
    def __init__(self, lyrics):
         self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            print('-' * 20)

song_1 = ["Happy Birthday to you", "I dont want you to get sued", "So I'll stop righ there."]
song_2 = ["They rally around the family", "With pockets full of shells"]

happy_bday = Song(song_1)

bulls_on_parade = Song(song_2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

