def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    my_list = list(phrase)
    return_string = ""
    
    reversed = my_list[::-1]
    for i in reversed:
        return_string += i
    return return_string    


