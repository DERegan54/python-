def digit_count(num):
    """ sorts num and counts occurence of each digit"""
    
    count = {}

    for digit in num:
        count[digit] = count.get(digit, 0) + 1

    return count  

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return digit_count(str(num1)) == digit_count(str(num2))





