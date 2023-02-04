def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    mult_list = [num for num in nums if num % 2 == 0]
    if len(mult_list) == 0:
        return 1
    elif len(mult_list) == 1:
        return mult_list[0]
    else:
        i = 0
        num = 1
        while i < len(mult_list):
            num *= mult_list[i]
            i += 1
        return num

    # Funny story: here's a much easier way to do this
    # One feels like an idiot when they look at these

    # product = 1

    # for num in nums:
    #     if num % 2 == 0:
    #         product = product * num

    # return product
