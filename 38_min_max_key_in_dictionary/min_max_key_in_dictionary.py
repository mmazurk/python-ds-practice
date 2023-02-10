def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # extract keys from dict, put in set, and order them. Then return first and last as tuple. 
    dict_keys = list(d.keys())
    dict_keys.sort()
    return tuple([dict_keys[0], dict_keys[len(dict_keys) - 1]])