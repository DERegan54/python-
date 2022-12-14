def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_dict = {}
    for ltr in phrase:
        letter_dict[ltr] = letter_dict.get(ltr, 0) + 1
    return letter_dict
