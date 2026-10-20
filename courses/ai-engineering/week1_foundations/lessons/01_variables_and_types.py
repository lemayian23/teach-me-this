# Lesson 1 - variables, types, printing
# Run it with:  python week1_foundations/lessons/01_variables_and_types.py

# A variable is a named box that holds one value.
name = "Denis"              # a string: text wrapped in quotes
age = 22                    # an int: a whole number
height_metres = 1.74        # a float: a number with a decimal point
is_learning = True          # a bool: True or False, always capital first letter

# print() shows something in the terminal.
print(name)

# type() tells you what kind of value something is.
print(type(age))

# f-string = fill in the blanks of a sentence. Note the f before the quotes.
print(f"{name} is {age} and tall? {is_learning}")

# Numbers can do maths; strings can be joined with + or repeated with *.
print(22 + 3)
print("ha" * 3)
