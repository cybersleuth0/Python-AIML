# ============================================================================
# FUNCTIONS IN PYTHON
# ============================================================================
# Functions are blocks of code that perform a specific task and can be 
# reused throughout a program. They help to break down complex problems 
# into smaller, more manageable pieces.
#
# Key concepts:
#   - def keyword: used to define a function
#   - parameters: variables listed inside the parentheses (inputs)
#   - return: sends a result back to the caller
#   - arguments: actual values passed to the function when called
# ============================================================================


# ----------------------------------------------------------------------------
# Q1: ADD TWO NUMBERS
# Task: Write a function that takes two numbers as arguments and returns their sum
# ----------------------------------------------------------------------------

# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
#
# print(add(5, 3))  # Output: 8


# ----------------------------------------------------------------------------
# Q2: CALCULATE AVERAGE
# Task: Write a function that returns the average of two numbers
# ----------------------------------------------------------------------------

# def average(a, b):
#     """Returns the average (mean) of two numbers."""
#     return (a + b) / 2
#
# print(average(10, 20))  # Output: 15.0


# ----------------------------------------------------------------------------
# Q3: NON-DEFAULT PARAMETERS (Mandatory Arguments)
# Task: Write a function that requires ALL arguments to be passed
# Note: You MUST provide values for every parameter when calling the function
# ----------------------------------------------------------------------------

# def greet(name, age):
#     """Returns a greeting message with name and age — both are required."""
#     return f"Hello {name}, you are {age} years old!"
#
# print(greet("Ayush", 20))  # Output: Hello Ayush, you are 20 years old!
# print(greet("Ayush"))      # ❌ Error: missing 1 required argument


# ----------------------------------------------------------------------------
# Q4: DEFAULT PARAMETERS (Optional Arguments)
# Task: Write a function with default values for some parameters
# Note: Default parameters come AFTER non-default parameters
#       If you don't pass a value, the default is used
# ----------------------------------------------------------------------------

# def greet(name, age=18):
#     """Returns a greeting message — age is optional (defaults to 18)."""
#     return f"Hello {name}, you are {age} years old!"
#
# print(greet("Ayush", 20))   # Output: Hello Ayush, you are 20 years old! (uses passed value)
# print(greet("Ayush"))        # Output: Hello Ayush, you are 18 years old! (uses default)
# print(greet("Ayush", 25))   # Output: Hello Ayush, you are 25 years old! (overrides default)


# ----------------------------------------------------------------------------
# Q5: MIXED PARAMETERS (Non-Default + Default)
# Task: Write a function that calculates total price with optional tax rate
# Rule: Non-default parameters MUST come first, then default parameters
# ----------------------------------------------------------------------------

# def calculate_total(price, tax_rate=0.18):
#     """Returns total price after adding tax (default tax rate: 18%)."""
#     total = price + (price * tax_rate)
#     return total
#
# print(calculate_total(100))           # Output: 118.0 (uses default tax 18%)
# print(calculate_total(100, 0.05))     # Output: 105.0 (custom tax 5%)
# print(calculate_total(price=200))     # Output: 236.0 (keyword argument)

