# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

import random
lst = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        lst.append(str(x))

print(",".join(lst))

# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 


def temp_conversion(temp):
    degree = int(temp[:-1])
    i_convention = temp[-1]
    if i_convention.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        o_convention = "Fahrenheit"
    elif i_convention.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        o_convention = "Celsius"
    print(temp, "is", result, "in", o_convention)


temp_conversion("0C")

# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the
# prompt appears again until the guess is correct, on successful guess,
# user will get a "Well guessed!" message, and the program will exit.

target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(
        input('Guess a number between 1 and 10 until you get it right: '))
print('Well guessed!')

# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output : 
# Number of even numbers : 5
# Number of odd numbers : 4

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

odd = 0
even = 0
for x in numbers:
    if not x % 2:
        even += 1
    else:
        odd += 1

print("Number of even numbers :", even)
print("Number of odd numbers :", odd)

# Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
            {"class": 'V', "section": 'A'}]
for item in datalist:
    print("Type of ", item, " is ", type(item))

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement. 
# Expected Output : 0 1 2 4 5

for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x, end=' ')
print("\n")
