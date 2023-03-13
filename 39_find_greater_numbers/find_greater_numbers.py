def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    
    count = 0

    for item in range(len(nums)):
        for other_item in range(item + 1, len(nums)):
            if nums[other_item] > nums[item]:
                count += 1

    return count
    
    
    # return sum(any(x < y for y in nums[i:]) for i,x in enumerate(nums))
    # sum(any(x < o for num in nums[i:]) for i, num in enumerate(nums))
    
    # count = 0
    # for num in nums:
    #     for other_num in nums: 
    #         print(num)
    #         print(other_num)
    #     if num < other_num:
    #         count += 1
    # return count 