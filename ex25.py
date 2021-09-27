
#More practice with functions and variables:
#We import this script into another python script to run it.

def break_words(stuff):
    #these comments below are called documentation comments.
    """This function will break up words for us"""
    #split() unlike sorted() will take care of spaces when sorting a list. Uses the seperator specified. In this case ' ' 
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    #The sorted() method tries to sort the lsit in order. Can not sort mixed data types i.e. list with inetger & strings for example.
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    #pop(0) removes the first item on the list
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    #pop(-1) removes the last item on the list.
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last ones"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    