def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        if make_int == True:
            sum = round(a) + round(b)
            if message == None:
                return f"The result is {sum}"
            else:
                return message + f" {sum}"
        else:
            sum = a + b
            if message == None:
                return f"The result is {sum}"
            else:    
                return message + f" {sum}"
    
    elif operation == 'subtract':
        if make_int == True:
            difference = round(a) - round(b)
            if message == None:
                return f"The result is {difference}"
            else:
                return message + f" {difference}"
        else: 
            difference = a - b
            if message == None:
                return f"The result is {difference}"
            else:
                return message + f" {difference}"

    elif operation == 'multiply':
        if make_int == True:
            product = round(a) * round(b)
            if message == None:
                return f"the result is {product}"
            else:
                return message + f" {product}"
        else:
            product = a * b
            if message == None:
                return f"The result is {product}"
            else: 
                return message + f" {product}"

    elif operation == 'divide':
        if make_int == True:
            quotient = a // b
            if message == None:
                return f"The result is {quotient}"
            else:
                return message + f" {quotient}"
        else: 
            quotient = a / b
            if message == None:
                return f"The result is {quotient}"
            else:
                return message + f" {quotient}"

