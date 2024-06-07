def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    lowered_phrase = phrase.lower()
    trimmed_and_lowered = lowered_phrase.replace(" ", "")
    reversed = list(trimmed_and_lowered)[::-1]
    reversed_to_string = "".join(reversed)

    if (trimmed_and_lowered == reversed_to_string):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
