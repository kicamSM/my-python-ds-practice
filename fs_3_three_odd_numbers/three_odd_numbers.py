def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    
    length = len(nums)
    num_of_3 = [(nums[i], nums[i + 1], nums[i + 2]) for i in range(length - 2)]
    
    def check_if_sum_is_even(triplet):
        return sum(list(triplet)) % 2 != 0 
    filtered = [triplet for triplet in num_of_3 if check_if_sum_is_even(triplet)]
    return True if filtered else False
        
    
    
    # length = len(in_list)
    # return [(in_list[i], in_list[i + 1, in_list[i + 2]) for i in range(length - 2)]
    
    # length = len(nums)
    # num_of_3 = [(nums[i], nums[i + 1], nums[i + 2]) for i in range(length - 2)]
    # for tpl in num_of_3: 
    #     lsts = list(tpl)
    #     print(lsts)
    #     total = sum(lsts)
    #     print(total)
    #     print(total % 2)
    # odd = [tpl for tpl in num_of_3 if total % 2 == 1]  
    # if odd:
    #     return True
    # else: 
    #     return False
            
     
    
    
    # length = len(nums)
    # num_of_3 = [(nums[i], nums[i + 1], nums[i + 2]) for i in range(length - 2)]
    
    # check_list = []
    
    # for triplet in num_of_3: 
    #     total = sum(list(triplet))
    #     check_list.append(total % 2 != 0)
        
    # if all(check_list):
    #     return True
    # else: 
    #     return False
    

    
    # length = len(nums)
    # num_of_3 = [(nums[i], nums[i + 1], nums[i + 2]) for i in range(length - 2)]
    # for tpl in num_of_3: 
    #     lsts = list(tpl)
    #     print(lsts)
    #     total = sum(lsts)
    #     print(total)
    #     print(total % 2)
    # if total % 2 == 1:
    #     return True 
    # else: 
    #     return False
     
   
    
    # if total % 2 == 0:
    # if any(total % 2 == 1 for lst in lsts): 
    #     return True
    # # if all(total % 2 != 0): 
    # #     return False
    # else: 
    #     return False
        
        
        # if all(total % 2 != 0 for lst in lsts): 
        
        # for lst in lsts:
        #     while lst in lsts != 0:
        #         return True 
        #     else:
        #         return False

        # for lst in lsts: 
        #     if total % 2 != 0: 
        #         return True 
        #     else: 
        #         return False
        # for num in tuple:
        #     print('print')
            # print(num)
            # total = sum(num)
    # print(total)
        # if total % 2 != 0:
        #     return True 
        # else:
        #     return False
    
    
    # start_idx = 0
    # end_idx = start_idx + 2
    # for num in nums:
    #     total = sum(nums[start_idx:end_idx])
    #     if total % 2 != 0:
    #         return True
    #     else: 
    #         return False 
        