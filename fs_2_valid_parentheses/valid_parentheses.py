def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # note: this returns the correct anaswer for each of their examples but not the correct answer for everything. Came up with example that would not return correct answer. Got some help on this and then went through their answer as well. 
    
    # if parens[0] != '(' or parens[-1] != ')':
    #     return False 
    # if parens.count(parens[0]) != parens.count(parens[-1]):
    #     return False 
    # else:
    #     return True
     
    # valid_parentheses('())(()')
    
      
    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0