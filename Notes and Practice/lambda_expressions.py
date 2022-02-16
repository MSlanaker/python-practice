# LAMBDA EXPRESSIONS:

# Useful when you need a short, throw away function that you may only use once.
# Common when sorting and filtering data.

# Let's say you want computer 3x+1

# Here's how you might do that with a normal function:
def f(x):
    return 3*x + 1


print(f(2))

# Or it can be done with a lambda expression (or anonymous function)

lambda x: 3*x + 1

# However, you can't call this because "lambda" is not the name of the function


# g = lambda x: 3*x + 1


# print(g(2))

# Another example:
# Combine first name and last name into a since "Full Name"

# full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

# print(full_name("  leonhard", "EULER"))

####################################################################################

# HOW TO ASSEMBLE ONE:

# lambda keyword, followed by the inputs, then a colon, then a single expression that
# acts as the return value. Cannot use for multi line functions
# lambda x, y: <expression>

#####################################################################################

# EXAMPLE
# Let's say we want to organize this list by last name, alphabetically
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke",
                 "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# We can call the help function to get more info on built-in methods like sort()
help(scifi_authors.sort)

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(scifi_authors)

######################################################################################

# EXAMPLE
