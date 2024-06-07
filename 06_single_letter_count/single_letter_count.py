def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    lowered_word = word.lower()
    return lowered_word.count(letter)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
