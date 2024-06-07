def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_as_list = list(phrase)
    phrase_as_list.reverse()
    answer = "".join(phrase_as_list)
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
