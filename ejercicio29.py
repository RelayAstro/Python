#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
def is_palindrome(input_string):
    # Replacing spaces with nothing
    single_word = input_string.replace(" ", "")

    # Converting the word to lower case
    single_word = single_word.lower()

    # Checking the first element with the last elements and so on
    for i in range(len(single_word)):
        if single_word[i] != single_word[len(single_word) - 1 - i]:
            return False
    return True

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True