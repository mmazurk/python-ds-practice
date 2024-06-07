def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_list = []

    for letter in phrase:
        if (letter.lower() == to_swap.lower()):
            if letter.isupper():
                letter = letter.lower()
            elif letter.islower():
                letter = letter.upper()
            swapped_list.append(letter)
        else:
            swapped_list.append(letter)

    swapped = "".join(swapped_list)
    return swapped


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
