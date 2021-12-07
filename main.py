# Import Statements
from PyDictionary import PyDictionary
import enchant

# Variable for controlling for loop
running = True
# english dictionary for checking words
d = enchant.Dict("en_US")
# English dictionary for checking meaning
english_dictionary = PyDictionary()


# Checks if an input word is an actual word
def check_word_validity(word):
    return d.check(word)


# Returns a word's meaning
def find_word_meaning(word):
    return english_dictionary.meaning(word)


# Checks to see if a word has the specified part of speech meaning
def check_word_type_validity(word, word_type):
    # If it does, returns true
    try:
        english_dictionary.meaning(word)[word_type]
        return True
    # Else, returns false
    except KeyError:
        return False


# Main For loop
while running:
    # User input word to lookup
    user_word = input("What word would you like to lookup? If finished, type 'e' to exit\n")
    # Exits if the user inputed 'e'
    if user_word == "e":
        running = False
    # If its not, checks if the word is valid
    elif check_word_validity(user_word):
        # If it is, prints the word's meaning
        print(find_word_meaning(user_word))
    # Else, lets the user know its not valid
    else:
        print("That is not a valid word")
