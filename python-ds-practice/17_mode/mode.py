def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    num_frequency = {}

    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1
    
    max_frequency = max(num_frequency.values())

    for (num, freq) in num_frequency.items():
        if freq == max_frequency:
            return num
        
    
        

        
