def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    upper_let = to_swap.upper()
    lower_let = to_swap.lower()
    return_value = []

    for letter in phrase:
        if letter == upper_let:
            return_value.append(letter.lower())
        elif letter == lower_let:
            return_value.append(letter.upper())
        else:
            return_value.append(letter)
    return "".join(return_value) 

