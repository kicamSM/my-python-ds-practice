def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel = 'aeiou'
    phrase.lower()
    x = 0
    in_dict = {}.fromkeys(vowel, 0)
    for letter in phrase: 
        if letter in in_dict: 
            in_dict[letter] += 1
    return {k: v for k, v in in_dict.items() if v != x}
    