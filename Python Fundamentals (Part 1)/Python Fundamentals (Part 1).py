
# ============================================================================
# PYTHON FUNDAMENTALS - ASSIGNMENT 1
# Write clear and well-commented code for each problem below
# ============================================================================

# Q1: NAME AND AGE GREETING
# Task: Ask the user for their name and age
# Then print a sentence like: "Hello Shradha, you are 21 years old!"
# Hint: Use input() to get name and age, convert age to int, then print them together

# Write your code here:

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# print(f'Hello {name}, you are {age} years old!')


# ============================================================================
# Q2: ARITHMETIC OPERATIONS
# Task: Take two numbers as input from the user
# Print their: sum, difference, product, and quotient
# Example: If user enters 10 and 5, print:
#   Sum: 15
#   Difference: 5
#   Product: 50
#   Quotient: 2.0

# Write your code here:

# a=input('Enter first number: ')
# b=input('Enter second number: ')
# sum = float(a) + float(b)
# difference = float(a) - float(b)
# product = float(a) * float(b)
# quotient = float(a) / float(b)
# print(f'Sum: {sum}')
# print(f'Difference: {difference}')
# print(f'Product: {product}')
# print(f'Quotient: {quotient}')

# ============================================================================
# Q3: AVERAGE OF THREE NUMBERS
# Task: Ask the user to enter two integers and one float
# Convert ALL of them to float type
# Calculate and print their average
# Example: 5, 10, 3.5 → Average: 6.166666...

# Write your code here:
# a=int(input("Enter first integer: "))
# b=int(input("Enter second integer: "))
# c=float(input("Enter float: "))
# average = (a + b + c) / 3
# print(f'Average: {average}')

# ============================================================================
# Q4: TYPE CONVERSION
# Task: The user enters a string containing a number (e.g., "45")
# Convert it to:
#   • An integer
#   • A float
#   • Keep it as a string again
# Print all three values along with their data types using type()

# Write your code here:

# input_str = input("Enter a number as a string: ")
# as_integer = int(input_str)
# as_float = float(input_str)
# as_string = str(input_str)

# print(f'Integer: {as_integer}, Type: {type(as_integer)}')
# print(f'Float: {as_float}, Type: {type(as_float)}')
# print(f'String: {as_string}, Type: {type(as_string)}')


# ============================================================================
# Q5: EXPRESSION EVALUATION
# Task: Evaluate and print the result of this expression: x = 10 + 3 * 2**2
# Explain in comments why you get that result (follow BODMAS/PEMDAS rules)
# BODMAS: Brackets, Orders(Exponents), Division, Multiplication, Addition, Subtraction

# Write your code here:

# x = 10 + 3 * 2**2
# Explanation:
# According to BODMAS/PEMDAS:
# 1. First, we evaluate the exponent: 2**2 = 4
# 2. Then we do the multiplication: 3 * 4 = 12
# 3. Finally, we do the addition: 10 + 12 = 22
# So the final value of x is 22
# print(x)


# ============================================================================
# Q6: SWAP TWO NUMBERS
# Task: Take values of two numbers entered by the user
# Swap them (exchange their values)
# Print the values before and after swapping
# Example: Before: a=5, b=10 → After: a=10, b=5

# Write your code here:
a = input("Enter first number: ")
b = input("Enter second number: ")

print(f'Before: a={a}, b={b}')
swap = a
a=b
b=swap
print(f'After: a={a}, b={b}')


# ============================================================================
# Q7: CELSIUS TO FAHRENHEIT
# Task: Ask the user for a temperature in Celsius (as string input)
# Convert it to float
# Calculate temperature in Fahrenheit using the formula:
# Fahrenheit = (Celsius * (9/5)) + 32
# Print the result

# Write your code here:




# ============================================================================
# Q8: AREA OF A CIRCLE
# Task: Take the radius (r) as user input
# Print the area of the circle using the formula:
# Area = π * r²
# Use π = 3.14

# Write your code here:




# ============================================================================
# Q9: SIMPLE INTEREST CALCULATION
# Task: Ask the user for:
#   • Principal (P) - the initial amount
#   • Rate (R) - the interest rate per year
#   • Time (T) - the time period in years
# Convert all to float
# Calculate Simple Interest using the formula:
# SI = (P * R * T) / 100
# Print the result

# Write your code here:




# ============================================================================
# Q10: EXTRACT INTEGER AND FRACTIONAL PARTS
# Task: Take a decimal number as input (like 45.78)
# Output:
#   • Integer part: 45
#   • Fractional part: 0.78
# Hint: Use int() to get integer part, subtract to get fractional part

# Write your code here: