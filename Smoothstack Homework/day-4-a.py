# 1.Create a function func() which prints a text ‘Hello World’

def hello():
    print("Hello World")


hello()

# 2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’


def hello(name):
    print("Hi, my name is " + name)


hello("Google")

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)


# 4.define a function func4(x,y) which returns the product of both the values.

def func4(x, y):
    return x + y


print(func4(5, 10))

# 5.define a function called as is_even that takes one argument , which returns true when even values is passed and false if it is not.


# 6.define a function that takes two arguments ,and returns true if the first value is greater than the second value and returns false if it is less than or equal to the second.

def check_greater(x, y):
    if x > y:
        return True
    else:
        return False


print(check_greater(65, 75))

# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.


def sum_of(*args):
    addition = 0
    for arg in args:
        addition += arg
    return addition


print(sum_of(5, 10, 15, 20))


# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.

def even(*args):
    even_list = []
    for i in list(args):
        if not i % 2:
            even_list.append(i)
    return even_list


print(even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 9.Define a function that takes a string and returns a matching string where every even letter is uppercase and every odd letter is lowercase
# <<give the python notebook exercises which are discussed  in .ipyb>>


# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.


# 11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.


# 12.Given a value,return a value which is twice as far as other side of 7


# 13.A function that capitalizes first and fourth character of a word in a string.
