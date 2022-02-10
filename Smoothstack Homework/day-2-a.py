# Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.

print("Hello World"[8])

# String slicing to grab the word ‘ink’ from the word  ‘thinker’

print("thinker"[2:5])

# S=’hello’,what is the output of h[1]

# S=’Sammy’ what is the output of s[2:]”

# Answer: The output would be mmy

s = "Sammy"
print(s[2:])

# With a single set function can you turn the word ‘Mississippi’ to distinct character word.

print(set("Mississippi"))

# Determine whether a phrase represents a palindrome or not.


print("Hello world"[::-1])

input_string = "Stars"


def pal_check(some_string):
    some_string = some_string.lower().replace(' ', '')
    if some_string == some_string[::-1]:
        print("Y")
    else:
        print("N")


pal_check(input_string)


input_data = """
3
Stars
O, a kak Uwakov lol vo kawu kakao!
Some men interpret nine memos
"""
pal_check(input_data)
