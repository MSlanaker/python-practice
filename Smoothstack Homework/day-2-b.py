# Create a list with one number, one word and one float value. Display the output of the list.

my_list = [3, "Hello", 4.5]
print(my_list)

# I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.

# nest_list = [1, 1, [1, 2]]
# print(str(nest_list[1][1])) - COME BACK TO

# lst=['a','b','c'] What is the result of lst[1:]?

# Answer: ['b', 'c']
lst = ['a', 'b', 'c']
print(lst[1:])

# Create a dictionary with weekdays an keys and week index numbers as values.
# Do assign dictionary to a variable

week_dictionary = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}

print(week_dictionary)

# D={‘k1’:[1,2,3]} what is the output of d[k1][1]

# Answer: 2
D = {"k1": [1, 2, 3]}
print(D["k1"][1])

# Can you create a list [1,[2,3]] into a tuple

simple_list = [1, [2, 3]]

simple_tuple = tuple(simple_list)
print(simple_tuple)

# With a single set function can you turn the word ‘Mississippi’ to distinct character word.

print(set("Mississippi"))
