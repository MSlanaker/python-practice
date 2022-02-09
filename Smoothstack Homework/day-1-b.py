# Numbers: Example code to add two numbers 50+50 and 100-10 and print it.

print(50 + 50)

print(100 - 10)

# ⦁	30+*6,6^6,6**6,6+6+6+6+6+6

print(30 + 6)

print(6 ^ 6)

print(6 ** 6)

print(6 + 6 + 6 + 6 + 6 + 6)

# Print “Hello World” on the console output. Print output “Hello World : 10”

print("Hello World")

print("Hello World:" + str(10))


# Input data contains values for loan size P, interest rate R and length of time to pay out L in months.
# Answer should contain the required monthly payment M rounded up to whole dollars (i.e. if you get non-integer result, increase it to nearest integer which is greater).

# Example input data: 800000 6 103

# First, we take in the input data
loan_amount = 800000
interest_rate = 6
repayment_length = 103

# Take the interest rate of 6, and convert it to a decimal of .06 by dividing by 100.
# Then, divide by twelve for the monthly interest.
interest_calculation = interest_rate / 100 / 12

# Take the months entered and convert to years, save as a variable.
years = repayment_length / 12

# Plug the variables into a formula to solve for the monthly payment
monthly_payment = loan_amount * (interest_calculation * (
    1 + interest_calculation) ** years) / ((1 + interest_calculation) ** years - 1)

# Call Python's built-in round() function and print the rounded total to the nearest whole dollar
print(round(monthly_payment))
