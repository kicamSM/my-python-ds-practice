def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out
    
    # list_phrase = list(phrase)
    # for char in list_phrase:
    #     if char == to_swap and char.isupper():
    #         char = char.lower()
    #         print(char)
    #     else:
    #         char.upper() in phrase 
    #         print(phrase)
    
    
    # list_phrase = list(phrase)
    # print(list_phrase)            
    # for char in list_phrase: 
    #     if char == to_swap.upper():
    #         # print(char.lower())
    #         list_phrase.replace(char, to_swap.lower())
    #     if char == to_swap.lower():
    #         # print(char.upper())
    #         list_phrase.replace(char, to_swap.upper())
    #         print(list_phrase)

    # if to_swap.isupper()
    #     phrase.replace(to_swap, to_swap.lower())
    
    
    # if to_swap.isupper():
    #     phrase.replace(to_swap, to_swap.lower())
    #     phrase.replace(to_swap.lower(), to_swap.upper())
    #     print(phrase)
    # if to_swap.islower():
    #     phrase.replace(to_swap, to_swap.upper())
    #     phrase.replace(to_swap.lower(), to_swap.upper())
    #     print(phrase)
            
    
    # phrase.replace(to_swap.upper(), to_swap.lower())
    # phrase.replace(to_swap.lower(), to_swap.upper())
    # print(phrase)

         