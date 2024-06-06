import doctest


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dictionary = {}
    for letter in phrase:
        letter_dictionary[letter] = letter_dictionary.get(letter, 0) + 1

    return letter_dictionary


if __name__ == "__main__":
    doctest.testmod()
    print("Test done, for better or worse!")
