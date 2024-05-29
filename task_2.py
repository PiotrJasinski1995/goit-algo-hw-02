from collections import deque

def check_palindrome(text_to_check):
    if text_to_check == None or not len(text_to_check):
        return False

    checking_deque = deque(text_to_check.replace(' ', '').lower())

    while len(checking_deque) > 1:
        first_character = checking_deque.popleft() 
        second_character = checking_deque.pop()

        if first_character != second_character:
            return False
    
    return True


print('Result for " ":', check_palindrome(''))
print('Result for "a":', check_palindrome('a'))
print('Result for "aa":', check_palindrome('aa'))
print('Result for "aba":', check_palindrome('aba'))
print('Result for "ba":', check_palindrome('ab'))
print('Result for "radar":', check_palindrome('kayak'))
print('Result for "madam":', check_palindrome('radar'))
print('Result for "refer":', check_palindrome('level'))
print('Result for "no lemon, no melon":', check_palindrome('no lemon, no melon'))
print('Result for "Mother has a son":', check_palindrome('Mother has a son'))
print('Result for "Eva can I see bees in a cave":', check_palindrome('Eva can I see bees in a cave'))
print('Result for "Able was I ere I saw Elba":', check_palindrome('Able was I ere I saw Elba'))
