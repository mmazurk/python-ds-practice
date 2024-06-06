def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    if len(lst) == 0:
        return
    return lst[len(lst) - 1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Test done, for better or worse!")
