# ============================================================================
# TYPES OF FUNCTIONS IN PYTHON
# ============================================================================
# Functions in Python can be categorized into different types based on their
# behavior, parameters, and return values. Understanding these types helps
# in writing clean, reusable, and well-structured code.
# ============================================================================


# ----------------------------------------------------------------------------
# TYPE 1: FUNCTION WITH NO ARGUMENTS AND NO RETURN VALUE
# Task: A function that only performs an action (like printing) but doesn't
#       take any input and doesn't return any value
# Use case: Display messages, print menus, log events
# ----------------------------------------------------------------------------

# def greet():
#     """Prints a greeting message — no input, no return value."""
#     print("Hello, welcome to Python!")
#
# greet()  # Output: Hello, welcome to Python!
# result = greet()  # Output: Hello, welcome to Python!
# print(result)     # Output: None (because there's no return statement)


# ----------------------------------------------------------------------------
# TYPE 2: FUNCTION WITH NO ARGUMENTS BUT WITH RETURN VALUE
# Task: A function that doesn't take input but returns a value
# Use case: Get current date/time, fetch a default configuration
# ----------------------------------------------------------------------------

# def get_pi():
#     """Returns the value of PI — no input required."""
#     return 3.14159
#
# pi = get_pi()
# print(f"Value of PI: {pi}")  # Output: Value of PI: 3.14159


# ----------------------------------------------------------------------------
# TYPE 3: FUNCTION WITH ARGUMENTS BUT NO RETURN VALUE
# Task: A function that takes input but only performs an action (doesn't return)
# Use case: Printing formatted messages, updating a file, sending emails
# ----------------------------------------------------------------------------

# def display_info(name, age):
#     """Prints user info — takes input but doesn't return anything."""
#     print(f"Name: {name}, Age: {age}")
#
# display_info("Ayush", 20)  # Output: Name: Ayush, Age: 20
# result = display_info("Ayush", 20)
# print(result)  # Output: None


# ----------------------------------------------------------------------------
# TYPE 4: FUNCTION WITH ARGUMENTS AND RETURN VALUE
# Task: A function that takes input AND returns a result
# Use case: Mathematical calculations, data processing, validation
# ----------------------------------------------------------------------------

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
#
# result = add(5, 3)
# print(f"Sum: {result}")  # Output: Sum: 8


# ----------------------------------------------------------------------------
# TYPE 5: FUNCTION WITH MULTIPLE RETURN VALUES
# Task: A function that returns multiple values (as a tuple)
# Use case: Returning min & max, quotient & remainder, coordinates
# ----------------------------------------------------------------------------

# def min_max(numbers):
#     """Returns both minimum and maximum values from a list."""
#     return min(numbers), max(numbers)
#
# smallest, largest = min_max([3, 1, 7, 2, 9])
# print(f"Min: {smallest}, Max: {largest}")  # Output: Min: 1, Max: 9


# ----------------------------------------------------------------------------
# TYPE 6: LAMBDA (ANONYMOUS) FUNCTION
# Task: A small, one-line function without a name
# Syntax: lambda arguments: expression
# Use case: Short operations like sorting, filtering, mapping
#
# EASY SYNTAX BREAKDOWN:
#   lambda  arguments  :  expression
#   ↑       ↑           ↑
#   keyword  inputs     what to do with inputs (auto-returned)
#
# Think of it as:
#   normal function:          def f(x): return x * 2
#   same lambda:              f = lambda x: x * 2
#
# Key difference: lambda automatically returns the result — no need to write 'return'
# ----------------------------------------------------------------------------

# # Basic lambda
# square = lambda x: x ** 2
# print(square(5))  # Output: 25

# # Lambda with multiple arguments
# multiply = lambda a, b: a * b
# print(multiply(4, 3))  # Output: 12

# # Lambda used in built-in functions
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(f"Squared: {squared}")  # Output: Squared: [1, 4, 9, 16, 25]

# # Lambda for filtering
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(f"Evens: {evens}")  # Output: Evens: [2, 4]


# ----------------------------------------------------------------------------
# TYPE 7: RECURSIVE FUNCTION
# Task: A function that calls itself
# Use case: Factorial, Fibonacci, tree traversal, divide & conquer algorithms
# ----------------------------------------------------------------------------

# def factorial(n):
#     """Returns the factorial of a number using recursion."""
#     # Base case: stops recursion
#     if n == 0 or n == 1:
#         return 1
#     # Recursive case: function calls itself
#     return n * factorial(n - 1)
#
# print(f"Factorial of 5: {factorial(5)}")  # Output: Factorial of 5: 120
# # 5 * 4 * 3 * 2 * 1 = 120


# ----------------------------------------------------------------------------
# TYPE 8: HIGHER-ORDER FUNCTION
# Task: A function that takes another function as an argument OR returns a function
# Use case: Decorators, callbacks, function factories
# ----------------------------------------------------------------------------

# # Function that accepts another function as argument 
# def operate(a, b, func):
#     """Performs an operation on a and b using the provided function."""
#     return func(a, b)
#
# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# print(operate(10, 5, add))      # Output: 15
# print(operate(10, 5, subtract)) # Output: 5

