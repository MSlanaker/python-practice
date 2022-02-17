# Day 5 –Weekend exercise work – please use functions for this problem

# Let us apply our programming skills to some quasi-scientific problem -
# since it is bit dull to learn only abstract things.

# The simple measure of body constitution was proposed at the middle of XIX century.
# It depends only on the height and weight of a person -
# and is called Body Mass Index or BMI. It is defined as:

# BMI = weight/height^2

# Where weight is taken in kilograms and height in meters.

# Four general grades are proposed:

# Underweight               BMI < 18.5
# Normal weight     18.5 <= BMI < 25.0
# Overweight        25.0 <= BMI < 30.0
# Obesity           30.0 <= BMI

# For example, if I have weight of 80 kg and height of 1.73 m I can calculate:
# BMI = 80 / (1.73)^2 = 26.7
# Overweight

# Input data contain number of people in the first line.
# Other lines will contain two values each - weight in kilograms and height in metres.
# Answer should contain words under, normal, over, obese for each
# corresponding test-case, separated with spaces.
# For example:

# Input data:

# 3
# 80 1.73
# 55 1.58
# 49 1.91

# Answer:

# over normal under

# num_people = input("How many people are you testing today? Please enter: ")

# hw_data = []

# hw_data.append(input(
#     "Please enter the height and weight of the first person, separated with a space: ").split())
# hw_data.append(input(
#     "Please enter the height and weight of the second person, separated with a space: ").split())
# hw_data.append(input(
#     "Please enter the height and weight of the third person, separated with a space: ").split())

# print(hw_data)

hw_data = [[80, 1.73], [55, 1.58], [49, 1.91]]

bmi_list = []


def bmi_calc(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def do_calculation(data):
    for person in data:
        bmi_list.append(bmi_calc(person[0], person[1]))


do_calculation(hw_data)

# print(bmi_list)


def output(list):
    for x in list:
        if x < 18.5:
            print("Under")
        elif x >= 18.5 and x < 25.0:
            print("Normal")
        elif x >= 25.0 and x < 30.0:
            print("Over")
        elif x >= 30.0:
            print("Obese")


print(output(bmi_list))
