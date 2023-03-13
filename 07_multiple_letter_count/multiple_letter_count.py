def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dictionary = {}
    for letter in phrase: 
        if letter in dictionary: 
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

 # dictionary = {}
    # for letter in phrase: 
    #     dictionary[letter] = dictionary.get(letter, 0) + 1
    # return dictionary

    # for letter in phrase:
    #     num = phrase.count(letter)
    #     print(num)
    # print(num)
    
    
    #     dictionary = {}.fromkeys(phrase, num)
    # print(dictionary)
    # for letter in phrase:
    #     dictionary[letter] == dictionary.get(i, 0) + 1
    #     return dictionary
    
