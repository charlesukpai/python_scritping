#Phrases used in OOP:
#is-a --> A phrase to say that something inherits from another, as in a “salmon” is-a “fish.”
#has-a --> A phrase to say something is composed of other things or has a trait, as in “a salmon has-a mouth.”
#class X(Y) --> “Make a class named X that is-a Y.”
#class X(object) --> def __init__(self, J) “class X has-a __init__ that takes self and J parameters.”
#class X(object) --> def M(self, J) “class X has-a function named M that takes self and J parameters.”
#foo = X() --> Set foo to an instance of class X
#foo.M(J) --> From foo, get the M function and call it with parameters self, J.
#foo.K = Q --> From foo, get theK attribute and assign it to Q

#Import the python modules we need
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#This checks to see how many arguements passed to argv and if one of them is "english"
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST =  True
else:
    PHRASE_FIRST = False

#Get the words from the web url and adds them to the empty list WORDS
#The strip method removes any leading or trailing spaces, encoding specifies what encoding to use for the strings.
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
                    random.sample(WORDS, snippet.count("%%%"))]
    
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        #Fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        #Fake other names:
        for word in other_names:
            result = result.replace("***", word, 1)

        #Fake parameter list:
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)

            input(">>> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")


