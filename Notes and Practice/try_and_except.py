# TRY/EXCEPT STRUCTURE

# You surround a dangerous section of code with try and except
# If the code in the try works - the except is skipped
# If the code in the try fails - it jumps to the except section

###################################################################################

# EXAMPLE

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)

##################################################################################

# BE CAREFUL about putting multiple lines within the try block.
# Python will go through each line and as soon as one blows up it'll jump to the except.
# This means that it could potentially skip over a working line of code in the try.

##################################################################################

# EXAMPLE

rawstr = input("Enter a number:")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a number")
