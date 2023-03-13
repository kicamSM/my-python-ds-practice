def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    # count = 0
    # if letter.lower() in word.lower():
    #     for letter in word: 
    #         count += 1 
    #     print(count)
    # else:
    #     print(0)
    lst = []
    lst.extend(word.lower())
    lower_letter = letter.lower()
    print(lst.count(lower_letter))
    