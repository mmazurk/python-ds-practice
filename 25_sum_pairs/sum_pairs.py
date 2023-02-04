def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    for number in nums:
        for iteration in range(len(nums) - 1):
            if number + nums[iteration + 1] == goal:
                return (number, nums[iteration + 1])
    return ()

    """
    The answer to this is a mathematical trick that I did't know. 
    You subtract each element from the goal and then add the element to the set;
    as you do this, you check if the difference is already in the set.
    If the difference is already in the set you return the element and difference. 
    
    I would have never figured this out.
    """


