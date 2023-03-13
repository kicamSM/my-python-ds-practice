from itertools import product

def make_pairs(in_list):
        return product(in_list, in_list)

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
    all_pairs = make_pairs(nums)
    filtered_pairs = [pair for pair in all_pairs if pair[0] + pair[1] == goal]
    if not filtered_pairs:
        return tuple()
    
    def sorter(pair):
        return max(nums.index(pair[0]), nums.index(pair[1]))
        
    return sorted(filtered_pairs, key=sorter)[0]



# if __name__ == "__main__":
#     nums = [5, 1, 4, 8, 3, 2]
#     print(sum_pairs(nums, 7))
        
        
    # sorted_pairs = sorted(filtered_pairs, key=lambda pair: nums.index(pair[1]))
    # return sorted_pairs
    # next starts calling it as an iterable object 


    # generator functions syntax like list cmprehension but use parethensis returns generator function product returns generator function
    
    # calling list stores everything
        

    
    
    # length = len(nums)
    # return [(nums[i], nums[]) for i in range(length - 1)]

    
    
    
    
    
    # for num in nums:
    #     for other_num in nums:
    #         if num + other_num == goal:
    #             return num, other_num