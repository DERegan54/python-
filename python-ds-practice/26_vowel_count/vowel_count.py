def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    VOWELS = ['a', 'e', 'i', 'o', 'u']
    lower_phrase = phrase.lower()
    vowel_frequency = {}

    for ltr in lower_phrase:
        if ltr in VOWELS:
            vowel_frequency[ltr] = vowel_frequency.get(ltr, 0) +1
    
    return vowel_frequency
        






    