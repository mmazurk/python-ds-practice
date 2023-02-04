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
    current_mode = 0
    for number in nums:
        count_of_number = nums.count(number)
        if count_of_number > current_mode:
            current_mode = number
    return current_mode

    # It's .py a la mode! 
        

        