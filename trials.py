"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given list."""
    
    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return an list of all even numbers."""

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """Given a list, return all elements at odd numbered indices."""
    result = []
    
    # for i in range(0, len(items)):
    #     if i % 2 != 0:
    #         result.append(items[i])

    for i, item in enumerate(items):
        if i % 2 != 0:
            result.append(item)

    return result

    # for lists: 
        # for i, item in enumerate(items):

    # for dictionaries: 
        # for i, item in items.item(): (key: value pairs)



def print_as_numbered_list(items):
    """Given a list, output a numbered list."""

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    """Return a list of numbers in a certain range."""

    nums = []
    i = 0

    for i in range(start, stop):
        nums.append(i)

    return nums

def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'"""
    
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case."""

    camelCase = []
    string = string.split("_")
    
    for word in string:
        camelCase.append(f"{word[0].upper()}{word[1:]}")

    return "".join(camelCase)

def longest_word_length(words):
    """Return the length of the longest word in the given list of words"""

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest


def truncate(string):
    """Truncate repeating characters into one character."""

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) - 1]:
            result.append(char)

    return "".join(result)


def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced."""

    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

    return parens == 0


def compress(string):
    """Return a compressed version of the given string."""

    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count >1:
        compressed.append(str(char_count))

    return ''.join(compressed)
