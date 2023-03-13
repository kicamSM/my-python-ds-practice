def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    list_phrase = list(phrase)
    new_list = list_phrase.copy()
    new_list.reverse()
    print(list_phrase)
    print(new_list)
    if list_phrase == new_list:
        print('True')
    else:
        print('False')

def is_palindrome2(phrase):
    return phrase == phrase[:: -1]

# much more simple way to do this