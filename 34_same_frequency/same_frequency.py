def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    string_num1 = list(str(num1))
    string_num1.sort()
    int1 = int("".join(string_num1))

    string_num2 = list(str(num2))
    string_num2.sort()
    int2 = int("".join(string_num2))

    if int1 - int2 == 0:
        return True
    else:
        return False
