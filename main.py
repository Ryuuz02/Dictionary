from PyDictionary import PyDictionary
import enchant

running = True
d = enchant.Dict("en_US")
english_dictionary = PyDictionary()


def check_word_validity(word):
    return d.check(word)


def find_word_meaning(word):
    return english_dictionary.meaning(word)


def check_word_type_validity(word, word_type):
    try:
        english_dictionary.meaning(word)[word_type]
        return True
    except KeyError:
        return False


while running:
    user_word = input("What word would you like to lookup? If finished, type 'e' to exit\n")
    if user_word == "e":
        running = False
    elif check_word_validity(user_word):
        print(find_word_meaning(user_word))
    else:
        print("That is not a valid word")
