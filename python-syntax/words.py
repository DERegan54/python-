

def  print_upper_words(words):
    """ For a list of words, print out each word on a separate line, in all uppercase letters
        words = [love, like, dislike, despise, indifferent]
        print_upper_words()
            LOVE
            LIKE
            DISLIKE
            DESPISE
            INDIFFERENT
    """

   
    for word in words:
        print(word.upper())
    
print_upper_words(['love', 'like', 'dislike', 'despise', 'indifferent'])


def print_upper_words_start_with_e(words):
    """ For a list of words, print out only words that start with the letters "e" or "E"
        words = [eleven, six, eight, seven, eighty, fourteen]
        print_upper_words_start_with_e(['eleven', 'six', 'eight', 'seven', 'eighty', 'fourteen'])
            ELEVEN
            EIGHT
            EIGHTY
     """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words_start_with_e(['eleven', 'six', 'eight', 'seven', 'eighty', 'fourteen'])


def print_upper_words_starting_with_letters(words, letters):
    """ Passing in a set of letters, the function should only print words that start with one of those letters
         words = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
         starts_with = M, W
         print_words_starting_with_user_choice(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
             MONDAY
             WEDNESDAY
    """
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words_starting_with_letters(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], letters=["M", "W"])

