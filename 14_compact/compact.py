def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # for item in lst:
    #     if not bool(item) or item != '()' or item != '[]':
    #         lst.remove(item) 
    # print(lst)
    
    # return [item for item in lst if bool(item) == True]

    # because item is true we can just say 
    
    return [item for item in lst if item]